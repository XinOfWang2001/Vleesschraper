package com.service_api.services;

import com.service_api.controllers.MeatController;
import com.service_api.data.data_stores.MeatPriceRepository;
import com.service_api.data.database_entities.AnalyticsMeatPrice;
import com.service_api.entities.LatestMeatPrice;
import com.service_api.entities.MeatPriceAggregation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class AggregatePriceService implements IAggregationPriceService{
    private final MeatPriceRepository analyticsRepository;
    private static final Logger log = LoggerFactory.getLogger(AggregatePriceService.class);
    // Cache
    // Relational database

    public AggregatePriceService(MeatPriceRepository analyticsRepository){
        this.analyticsRepository = analyticsRepository;
    }

    //
    @Override
    public MeatPriceAggregation GetAggregate(){
        // Retrieve latest data.
        List<AnalyticsMeatPrice> results = analyticsRepository.findAll();
        log.info(String.valueOf(results.size()));
        // Map from database entities to Domain model.
        List<LatestMeatPrice> accumulator = results.stream().map(AnalyticsMeatPrice::ToDomain).toList();
        return new MeatPriceAggregation(accumulator);
    }
    //@ Method perform aggregate query on specific supermarket.
}
