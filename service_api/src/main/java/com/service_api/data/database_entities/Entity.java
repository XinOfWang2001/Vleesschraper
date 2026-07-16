package com.service_api.data.database_entities;

public interface Entity<Domain> {

    Entity<Domain> OfDomain(Domain domain);
    Domain ToDomain();
}
