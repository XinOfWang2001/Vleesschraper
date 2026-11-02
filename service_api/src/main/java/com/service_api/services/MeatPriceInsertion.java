package com.service_api.services;

import com.service_api.data.data_stores.MeatPriceRepository;
import com.service_api.data.database_entities.AnalyticsMeatPrice;
import com.service_api.entities.LatestMeatPrice;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MeatPriceInsertion implements IMeatPriceInsertion{
    private final MeatPriceRepository meatPriceRepository;

    public MeatPriceInsertion(MeatPriceRepository meatPriceRepository) {
        this.meatPriceRepository = meatPriceRepository;
    }

    @Override
    public void BulkInsert(List<LatestMeatPrice> meat) {
        List<AnalyticsMeatPrice> entities = meat.stream()
                .map(price -> new AnalyticsMeatPrice().OfDomain(price))
                .toList();
        meatPriceRepository.saveAll(entities);
    }
}
