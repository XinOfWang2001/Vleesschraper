package com.service_api.entities;

import java.time.LocalDateTime;

public record LatestMeatPrice(LocalDateTime date, String Meat, float CurrentPrice) {
}
