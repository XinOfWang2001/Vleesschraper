package com.service_api.entities;

import java.util.List;

public record MeatPriceAggregation(List<LatestMeatPrice> meatPrices) {
}
