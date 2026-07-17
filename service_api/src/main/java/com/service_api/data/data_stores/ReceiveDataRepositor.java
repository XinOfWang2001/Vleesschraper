package com.service_api.data.data_stores;

import com.service_api.data.database_entities.AnalyticsMeatPrice;
import org.springframework.data.repository.Repository;

public interface ReceiveDataRepositor extends Repository<AnalyticsMeatPrice, Long> {
}
