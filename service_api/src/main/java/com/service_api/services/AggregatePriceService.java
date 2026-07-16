package com.service_api.services;

import com.service_api.controllers.MeatController;
import com.service_api.data.data_stores.MeatPriceRepository;
import com.service_api.data.database_entities.AnalyticsMeatPrice;
import com.service_api.entities.LatestMeatPrice;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AggregatePriceService {
    private final MeatPriceRepository analyticsRepository;
    private static final Logger log = LoggerFactory.getLogger(AggregatePriceService.class);
    // Cache
    // Relational database

    public AggregatePriceService(MeatPriceRepository analyticsRepository){
        this.analyticsRepository = analyticsRepository;
    }

    //@ Method perform aggregate query.
    public LatestMeatPrice GetAggregate(){
        List<AnalyticsMeatPrice> results = analyticsRepository.findAll();
        log.info(String.valueOf(results.size()));
        return results.getFirst().ToDomain();
    }
    //@ Method perform aggregate query on specific supermarket.
}
