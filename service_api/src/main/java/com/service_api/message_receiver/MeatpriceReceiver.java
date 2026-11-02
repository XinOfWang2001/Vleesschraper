package com.service_api.message_receiver;

import tools.jackson.core.JacksonException;
import tools.jackson.databind.JsonNode;
import tools.jackson.databind.ObjectMapper;
import com.service_api.entities.LatestMeatPrice;
import com.service_api.services.IMeatPriceInsertion;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component
public class MeatpriceReceiver {
    private static final Logger log = LoggerFactory.getLogger(MeatpriceReceiver.class);

    private final ObjectMapper objectMapper;
    private final IMeatPriceInsertion meatPriceInsertion;

    public MeatpriceReceiver(ObjectMapper objectMapper, IMeatPriceInsertion meatPriceInsertion) {
        this.objectMapper = objectMapper;
        this.meatPriceInsertion = meatPriceInsertion;
    }

    @KafkaListener(topics = "${app.kafka.topic}")
    public void receive(String message) {
        List<LatestMeatPrice> meatPrices;
        try {
            JsonNode payload = objectMapper.readTree(message);
            meatPrices = new ArrayList<>();

            if (payload.isArray()) {
                for (JsonNode item : payload) {
                    meatPrices.add(objectMapper.treeToValue(item, LatestMeatPrice.class));
                }
            } else if (payload.isObject()) {
                meatPrices.add(objectMapper.treeToValue(payload, LatestMeatPrice.class));
            } else {
                throw new IllegalArgumentException("Kafka payload must be a meat price object or an array of meat price objects");
            }
        } catch (JacksonException exception) {
            log.error("Failed to process meat price Kafka message", exception);
            throw new IllegalArgumentException("Failed to process meat price Kafka message", exception);
        }

        meatPriceInsertion.BulkInsert(meatPrices);
        log.info("Persisted {} meat price record(s) received from Kafka", meatPrices.size());
    }
}
