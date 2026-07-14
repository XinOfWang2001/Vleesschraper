package com.service_api.services;

import com.service_api.entities.LatestMeatPrice;
import org.springframework.stereotype.Service;

@Service
public class AggregatePriceService {
    // Cache
    // Relational database

    //@ Method perform aggregate query.
    public LatestMeatPrice GetAggregate(){
        return new LatestMeatPrice();
    }
    //@ Method perform aggregate query on specific supermarket.
}
