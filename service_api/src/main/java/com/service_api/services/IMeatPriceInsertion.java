package com.service_api.services;

import com.service_api.entities.LatestMeatPrice;

import java.util.List;

public interface IMeatPriceInsertion {
    void BulkInsert(List<LatestMeatPrice> meat);
}
