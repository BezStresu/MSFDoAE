#include "main.h"
#include "spi.h"
#include "usart.h"
#include "usb_otg.h"
#include "gpio.h"
#include "ad7606_stm32_JL.h"
#include "attenuators.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define NUM_MEASUREMENTS 50
#define NUM_CHANNELS 4
#define MAX_UART_LENGTH 10

uint16_t adc_data[NUM_CHANNELS];
uint32_t sum_data[NUM_CHANNELS] = {0};
uint16_t avg_data[NUM_CHANNELS];
uint8_t uart_received_char;

void SystemClock_Config(void);

void average_results() {
    memset(sum_data, 0, sizeof(sum_data));

    for (int measurement = 0; measurement < NUM_MEASUREMENTS; measurement++) {
        AD7606_Reset();
        AD7606_StartConversion();

        while (HAL_GPIO_ReadPin(BUSY_GPIO_Port, BUSY_Pin) == GPIO_PIN_SET) {}

        if (AD7606_ReadData(adc_data, NUM_CHANNELS)) {
            for (int i = 0; i < NUM_CHANNELS; i++) {
                sum_data[i] += adc_data[i];
            }
        } else {
            uint8_t error_msg[] = "Data reading error\r\n";
            HAL_UART_Transmit_IT(&huart3, error_msg, strlen((char*)error_msg));
            return;
        }

        HAL_Delay(5);
    }

    for (int i = 0; i < NUM_CHANNELS; i++) {
        avg_data[i] = (uint16_t)round((float)sum_data[i] / NUM_MEASUREMENTS);
    }
}

float value;
float part1, part2;

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) {
    static char received_str[10];
    static uint8_t index = 0;

    if (huart->Instance == USART3) {
        if (uart_received_char == 'm') {
            uint8_t komunikat[50];
            uint8_t dl_kom = 0;

            for (int i = 0; i < NUM_CHANNELS; i++) {
                dl_kom += sprintf((char*)(komunikat + dl_kom), "%u", avg_data[i]);
                if (i != NUM_CHANNELS - 1) {
                    dl_kom += sprintf((char*)(komunikat + dl_kom), " ");
                }
            }

            dl_kom += sprintf((char*)(komunikat + dl_kom), "\r\n");

            HAL_UART_Transmit_IT(&huart3, komunikat, dl_kom);
            HAL_GPIO_WritePin(GPIOB, LD2_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOB, LD3_Pin, GPIO_PIN_SET);
        }
        else if (uart_received_char == 'a') {
			   SetAttenuation(0.f, 1);
			   SetAttenuation(0.f, 2);
		}
	    else if (uart_received_char == 'b') {
			   SetAttenuation(0.5f, 1);
			   SetAttenuation(0.5f, 2);
		}
	    else if (uart_received_char == 'c') {
			   SetAttenuation(1.f, 1);
			   SetAttenuation(1.f, 2);
		}
        else if (uart_received_char == 'd') {
			   SetAttenuation(1.5f, 1);
			   SetAttenuation(1.5f, 2);
		}
	    else if (uart_received_char == 'e') {
			   SetAttenuation(2.f, 1);
			   SetAttenuation(2.f, 2);
		}
	    else if (uart_received_char == 'f') {
			   SetAttenuation(2.5f, 1);
			   SetAttenuation(2.5f, 2);
		}
        else if (uart_received_char == 'g') {
			   SetAttenuation(3.f, 1);
			   SetAttenuation(3.f, 2);
		}
	    else if (uart_received_char == 'h') {
			   SetAttenuation(3.5f, 1);
			   SetAttenuation(3.5f, 2);
		}
	    else if (uart_received_char == 'i') {
			   SetAttenuation(4.f, 1);
			   SetAttenuation(4.f, 2);
		}
	    else if (uart_received_char == 'j') {
			   SetAttenuation(4.5f, 1);
			   SetAttenuation(4.5f, 2);
		}
        else if (uart_received_char >= '0' && uart_received_char <= '9') {
            received_str[index++] = uart_received_char;

            if (index >= 2) {
                received_str[index] = '\0';

                char *endptr;
                long uart_value = strtol(received_str, &endptr, 10);

                if (*endptr == '\0' && uart_value >= 0 && uart_value <= 63) {
                    float part1 = uart_value / 2.0f;
                    float part2 = uart_value / 2.0f;

                    part1 = roundf(part1 * 2) / 2.0f;
                    part2 = roundf(part2 * 2) / 2.0f;

                    SetAttenuation(part1, 1);
                    SetAttenuation(part2, 2);
                } else {
                	return;
                }

                index = 0;
            }
        }
        else {
            HAL_GPIO_WritePin(GPIOB, LD1_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOB, LD2_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOB, LD3_Pin, GPIO_PIN_RESET);
        }

        HAL_UART_Receive_IT(&huart3, &uart_received_char, 1);
    }
}


int main(void) {
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_USART3_UART_Init();
    MX_USB_OTG_FS_PCD_Init();
    MX_SPI1_Init();

    AD7606_Init(&hspi1);

    SPI_Init_Att();

    float stage1 = 31.5f;
    float stage2 = 31.5f;

    SetAttenuation(stage1, 1);
    SetAttenuation(stage2, 2);


    HAL_UART_Receive_IT(&huart3, &uart_received_char, 1);
    HAL_GPIO_WritePin(GPIOB, LD1_Pin, GPIO_PIN_SET);

    while (1) {
        average_results();
    }
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_BYPASS;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 4;
  RCC_OscInitStruct.PLL.PLLN = 168;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 7;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_5) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
