/*
 * attenuators.h
 *
 *  Created on: Dec 16, 2024
 *      Author: User
 */

#ifndef INC_ATTENUATORS_H_
#define INC_ATTENUATORS_H_
#include "stm32f4xx_hal.h"
#include "gpio.h"
#include <stdint.h>

#define LE1_HIGH() HAL_GPIO_WritePin(GPIOB, LE1_Pin, GPIO_PIN_SET)
#define LE1_LOW() HAL_GPIO_WritePin(GPIOB, LE1_Pin, GPIO_PIN_RESET)
#define SIN1_HIGH() HAL_GPIO_WritePin(GPIOC, SIN1_Pin, GPIO_PIN_SET)
#define SIN1_LOW() HAL_GPIO_WritePin(GPIOC, SIN1_Pin, GPIO_PIN_RESET)
#define CLK1_HIGH() HAL_GPIO_WritePin(GPIOB, CLK1_Pin, GPIO_PIN_SET)
#define CLK1_LOW() HAL_GPIO_WritePin(GPIOB, CLK1_Pin, GPIO_PIN_RESET)

#define LE2_HIGH() HAL_GPIO_WritePin(GPIOB, LE2_Pin, GPIO_PIN_SET)
#define LE2_LOW() HAL_GPIO_WritePin(GPIOB, LE2_Pin, GPIO_PIN_RESET)
#define SIN2_HIGH() HAL_GPIO_WritePin(GPIOC, SIN2_Pin, GPIO_PIN_SET)
#define SIN2_LOW() HAL_GPIO_WritePin(GPIOC, SIN2_Pin, GPIO_PIN_RESET)
#define CLK2_HIGH() HAL_GPIO_WritePin(GPIOF, CLK2_Pin, GPIO_PIN_SET)
#define CLK2_LOW() HAL_GPIO_WritePin(GPIOF, CLK2_Pin, GPIO_PIN_RESET)

#define LE3_HIGH() HAL_GPIO_WritePin(GPIOC, LE3_Pin, GPIO_PIN_SET)
#define LE3_LOW() HAL_GPIO_WritePin(GPIOC, LE3_Pin, GPIO_PIN_RESET)
#define SIN3_HIGH() HAL_GPIO_WritePin(GPIOB, SIN3_Pin, GPIO_PIN_SET)
#define SIN3_LOW() HAL_GPIO_WritePin(GPIOB, SIN3_Pin, GPIO_PIN_RESET)
#define CLK3_HIGH() HAL_GPIO_WritePin(GPIOB, CLK3_Pin, GPIO_PIN_SET)
#define CLK3_LOW() HAL_GPIO_WritePin(GPIOB, CLK3_Pin, GPIO_PIN_RESET)

#define LE4_HIGH() HAL_GPIO_WritePin(GPIOB, LE4_Pin, GPIO_PIN_SET)
#define LE4_LOW() HAL_GPIO_WritePin(GPIOB, LE4_Pin, GPIO_PIN_RESET)
#define SIN4_HIGH() HAL_GPIO_WritePin(GPIOA, SIN4_Pin, GPIO_PIN_SET)
#define SIN4_LOW() HAL_GPIO_WritePin(GPIOA, SIN4_Pin, GPIO_PIN_RESET)
#define CLK4_HIGH() HAL_GPIO_WritePin(GPIOB, CLK4_Pin, GPIO_PIN_SET)
#define CLK4_LOW() HAL_GPIO_WritePin(GPIOB, CLK4_Pin, GPIO_PIN_RESET)

void Delay_ns(uint32_t ns);
void SPI_Init_Att();
void SPI_Write_Att(uint8_t data, uint8_t stage);
void SetAttenuation(float attenuation, uint8_t stage);


#endif /* INC_ATTENUATORS_H_ */
