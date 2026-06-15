# Vleesschraper

Welkom bij de **Vleesschraper** repository! Dit project is een "polyglot monorepo" dat bestaat uit twee hoofdonderdelen: 
- een Python-gebaseerde webscraper die productgegevens (zoals vleesproducten en filters) verzamelt.
- Spring Boot backend API om deze gegevens te verwerken en openbaar te maken voor het publiek.

---

## Project Structuur

De repository is opgedeeld in twee onafhankelijke applicaties om de codebases schoon en gescheiden te houden:

```text
Vleesschraper/
│
├── webscraper/             # Python Webscraper
│   ├── src/                # De logica van de webscrapers.
│   ├── tests/              # Unit tests (inclusief HTML mock fixtures)
│   └── requirements.txt    # Python afhankelijkheden
│
└── service_api/            # Spring Boot REST API (Java 25)
    ├── src/                # Java broncode (Controllers, Services, Models)
    ├── pom.xml             # Maven configuratie
    └── mvnw                # Maven Wrapper CLI script
