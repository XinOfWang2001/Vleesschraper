package com.service_api.services;

import com.service_api.entities.LatestMeatPrice;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MeatPriceInsertion implements IMeatPriceInsertion{
    @Override
    public void BulkInsert(List<LatestMeatPrice> meat) {

    }
}
