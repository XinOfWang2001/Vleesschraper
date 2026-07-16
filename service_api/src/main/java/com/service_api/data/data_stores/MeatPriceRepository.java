package com.service_api.data.data_stores;

import com.service_api.data.database_entities.AnalyticsMeatPrice;
import org.springframework.data.repository.ListCrudRepository;


public interface MeatPriceRepository extends ListCrudRepository<AnalyticsMeatPrice, Long> {
}
