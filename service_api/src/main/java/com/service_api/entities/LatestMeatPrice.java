package com.service_api.entities;

import java.time.LocalDateTime;

public record LatestMeatPrice(
        Long datecode,
        LocalDateTime date,
        String title,
        String capitalizedTitle,
        String supermarket,
        float normalPrice,
        float currentPrice,
        int discount,
        int weight
) {
}
