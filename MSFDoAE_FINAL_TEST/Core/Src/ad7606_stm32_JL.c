#include "ad7606_stm32_JL.h"

static SPI_HandleTypeDef *ad7606_hspi;

void AD7606_Init(SPI_HandleTypeDef *hspi) {
    ad7606_hspi = hspi;

    HAL_GPIO_WritePin(AD7606_RESET_Port, AD7606_RESET_Pin, GPIO_PIN_RESET);
    HAL_GPIO_WritePin(AD7606_CONVST_Port, AD7606_CONVST_Pin, GPIO_PIN_RESET);
    HAL_GPIO_WritePin(AD7606_CS_Port, AD7606_CS_Pin, GPIO_PIN_SET);

    AD7606_Reset();
    return;
}

void AD7606_Reset() {
    HAL_GPIO_WritePin(RESET_GPIO_Port, RESET_Pin, GPIO_PIN_SET);
    HAL_Delay(1);
    HAL_GPIO_WritePin(RESET_GPIO_Port, RESET_Pin, GPIO_PIN_RESET);
    HAL_Delay(1);
    return;
}

void AD7606_StartConversion(void) {
    HAL_GPIO_WritePin(AD7606_CONVST_Port, AD7606_CONVST_Pin, GPIO_PIN_SET);
    HAL_Delay(1);
    HAL_GPIO_WritePin(AD7606_CONVST_Port, AD7606_CONVST_Pin, GPIO_PIN_RESET);
    return;
}

bool AD7606_WaitForBusy(void) {
    uint32_t timeout = 1000000;
    while (HAL_GPIO_ReadPin(BUSY_GPIO_Port, BUSY_Pin) == GPIO_PIN_SET) {
        if (--timeout == 0) {
            return false;
        }
    }
    return true;
}

bool AD7606_ReadData(uint16_t *data, uint8_t num_channels) {
    if (num_channels > 4) { //
        return false;
    }

    HAL_GPIO_WritePin(AD7606_CS_Port, AD7606_CS_Pin, GPIO_PIN_RESET);

    uint16_t tmp_data = 0;

    for (uint8_t i = 0; i < num_channels; i++) {
        if (HAL_SPI_Receive(ad7606_hspi, (uint8_t *)&tmp_data, 1, HAL_MAX_DELAY) != HAL_OK) {
            HAL_GPIO_WritePin(AD7606_CS_Port, AD7606_CS_Pin, GPIO_PIN_SET);
            return false;
        }
        data[i] = tmp_data;
    }

    HAL_GPIO_WritePin(AD7606_CS_Port, AD7606_CS_Pin, GPIO_PIN_SET);
    return true;
}


