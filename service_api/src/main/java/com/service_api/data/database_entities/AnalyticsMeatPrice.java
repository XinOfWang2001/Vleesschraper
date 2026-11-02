package com.service_api.data.database_entities;

import com.service_api.entities.LatestMeatPrice;
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Column;
import org.springframework.data.relational.core.mapping.Table;

import java.time.LocalDateTime;
// @ The table format
@Table("Fact_Analytics_Meatprices")
public class AnalyticsMeatPrice implements Entity<LatestMeatPrice> {
    // PRIMARY KEY
    // UNIQUE (DateCode, Capitalized_Title) Surrogate key in combination with capitalized_title.
    @Id
    @Column("datecode")
    public Long datecode;
    @Column("date")
    public LocalDateTime date;
    @Column("title")
    public String title;
    // Surrogate key in combination with DateCode.
    @Column("capitalized_title")
    public String capitalized_Title;

    @Column("supermarket")
    public String supermarket;

    @Column("normal_price")
    public float normal_price;

    @Column("current_price")
    public float current_price;

    @Column("discount")
    public int discount;

    @Column("weight")
    public int weight;

    public AnalyticsMeatPrice() {}

    public AnalyticsMeatPrice(Long datecode, LocalDateTime date, String title, String capitalized_title, String supermarket, float normal_price, float current_price, int discount, int weight) {
        this.datecode = datecode;
        this.date = date;
        this.title = title;
        capitalized_Title = capitalized_title;
        this.supermarket = supermarket;
        this.normal_price = normal_price;
        this.current_price = current_price;
        this.discount = discount;
        this.weight = weight;
    }

    @Override
    public AnalyticsMeatPrice OfDomain(LatestMeatPrice latestMeatPrice) {
        return new AnalyticsMeatPrice(
                latestMeatPrice.datecode(),
                latestMeatPrice.date(),
                latestMeatPrice.title(),
                latestMeatPrice.capitalizedTitle(),
                latestMeatPrice.supermarket(),
                latestMeatPrice.normalPrice(),
                latestMeatPrice.currentPrice(),
                latestMeatPrice.discount(),
                latestMeatPrice.weight()
        );
    }

    @Override
    public LatestMeatPrice ToDomain() {
        return new LatestMeatPrice(
                datecode,
                date,
                title,
                capitalized_Title,
                supermarket,
                normal_price,
                current_price,
                discount,
                weight
        );
    }
}
