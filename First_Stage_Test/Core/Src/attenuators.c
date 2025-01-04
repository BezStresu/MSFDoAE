#include "attenuators.h"

void Delay_ns(uint32_t ns) {
    uint32_t cycles = (ns + 62) / 62;
    while (cycles--) {
        __NOP();
    }
}

void SPI_Init_Att() {
    LE1_HIGH();
    LE2_HIGH();
    LE3_HIGH();
    LE4_HIGH();

    SIN1_LOW();
    SIN2_LOW();
    SIN3_LOW();
    SIN4_LOW();

    CLK1_LOW();
    CLK2_LOW();
    CLK3_LOW();
    CLK4_LOW();

}

void SPI_Write_Att(uint8_t data, uint8_t stage) {
    if (stage != 1 && stage != 2) return;

    if (stage == 1) {
        LE1_LOW();
        LE3_LOW();
        Delay_ns(62);
        for (int i = 5; i >= 0; i--) {
            if (data & (1 << i)) {
                SIN1_HIGH();
                SIN3_HIGH();
            } else {
                SIN1_LOW();
                SIN3_LOW();
            }
            CLK1_HIGH();
            CLK3_HIGH();
            Delay_ns(62);
            CLK1_LOW();
            CLK3_LOW();
            Delay_ns(62);
        }
        LE1_HIGH();
        LE3_HIGH();
        Delay_ns(62);
        Delay_ns(630);
    } else if (stage == 2) {
        LE2_LOW();
        LE4_LOW();
        Delay_ns(62);
        for (int i = 5; i >= 0; i--) {
            if (data & (1 << i)) {
                SIN2_HIGH();
                SIN4_HIGH();
            } else {
                SIN2_LOW();
                SIN4_LOW();
            }
            CLK2_HIGH();
            CLK4_HIGH();
            Delay_ns(62);
            CLK2_LOW();
            CLK4_LOW();
            Delay_ns(62);
        }
        LE2_HIGH();
        LE4_HIGH();
        Delay_ns(62);
        Delay_ns(630);
    }
}

void SetAttenuation(float attenuation, uint8_t stage) {
    if (attenuation < 0.5f || attenuation > 31.5f) {
        return;
    }
    uint8_t data = (uint8_t)((attenuation / 0.5f) + 0.5f);
    SPI_Write_Att(data, stage);
}
