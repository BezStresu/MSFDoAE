#ifndef AD7606_STM32_JL_H
#define AD7606_STM32_JL_H

#include "stm32f4xx_hal.h"
#include "gpio.h"
#include <stdint.h>
#include <stdbool.h>

#define AD7606_RESET_Pin    RESET_Pin
#define AD7606_RESET_Port   GPIOF

#define AD7606_CONVST_Pin   CONV_Pin
#define AD7606_CONVST_Port  GPIOF

#define AD7606_BUSY_Pin     BUSY_Pin
#define AD7606_BUSY_Port    GPIOD

#define AD7606_CS_Pin       CS_Pin
#define AD7606_CS_Port      GPIOD

#define AD7606_MAX_CHANNELS 8

void AD7606_Init(SPI_HandleTypeDef *hspi);
void AD7606_Reset(void);
void AD7606_StartConversion(void);
bool AD7606_WaitForBusy(void);
bool AD7606_ReadData(uint16_t *data, uint8_t num_channels);

#endif

