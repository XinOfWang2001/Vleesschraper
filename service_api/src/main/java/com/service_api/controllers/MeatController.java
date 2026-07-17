package com.service_api.controllers;

import com.service_api.entities.LatestMeatPrice;
import com.service_api.entities.MeatPriceAggregation;
import com.service_api.services.AggregatePriceService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MeatController {

    private static final Logger log = LoggerFactory.getLogger(MeatController.class);
    private final AggregatePriceService aggregatePriceService;

    public MeatController(AggregatePriceService aggregatePriceService) {
        this.aggregatePriceService = aggregatePriceService;
    }
    /* @ Aim
    - Get latest meat-price of N-period back.
    - Default should be 6 months.
    - But can be 1 week to 3 years.
    * */
    @GetMapping("/meat-prices")
    public ResponseEntity<MeatPriceAggregation>  GetLatestMeatPrices(){
        try {
            log.info("Request received");
            // Default should be per supermarkets.
            // Here validation.
            // Return the average, minimum and maximum price of meat.
            MeatPriceAggregation result = aggregatePriceService.GetAggregate();
            return ResponseEntity.ok(result);
        } catch (Exception exc) {
            log.info("Request failed");
            return ResponseEntity.badRequest().build();
        }
    }
}
