# Portfolio Intelligence Dashboard - Project Description

## Introduction

The Portfolio Intelligence Dashboard is an advanced web-based application designed to provide comprehensive investment portfolio analysis and intelligent insights. In today's fast-paced financial markets, individual investors face the challenge of processing vast amounts of market data, news, and analytical information to make informed investment decisions. This project addresses the need for an integrated platform that combines real-time stock data, news sentiment analysis, and AI-powered investment advisory capabilities.

The application serves as a centralized hub for portfolio management, offering features such as stock price tracking, portfolio performance visualization, market news aggregation, and an intelligent chatbot that can answer complex investment questions using natural language processing and retrieval-augmented generation (RAG) technology.

## Problem Statement

Individual investors and portfolio managers face several critical challenges in today's investment landscape:

1. **Information Overload**: The sheer volume of financial news, market data, and analysis available makes it difficult to identify relevant information for specific portfolio holdings.

2. **Data Fragmentation**: Investment-related information is scattered across multiple platforms - stock prices on one site, news on another, and analytical tools on yet another platform. This fragmentation leads to inefficiency and potential missed opportunities.

3. **Lack of Contextual Intelligence**: Traditional portfolio tracking tools provide basic metrics but lack the ability to provide contextual insights that connect market news, company developments, and portfolio performance in a meaningful way.

4. **Technical Barriers**: Accessing and interpreting complex financial data often requires technical expertise in data analysis, API integration, and programming, creating barriers for average investors.

5. **Delayed Decision Making**: Without real-time data integration and intelligent analysis, investors may miss critical market movements or news that could impact their portfolio.

## Hypothesis

**Primary Hypothesis**: By integrating real-time stock market data, news sentiment analysis, and AI-powered natural language query capabilities into a single unified platform, we can significantly improve investment decision-making efficiency and quality for individual portfolio managers.

**Supporting Hypotheses**:

1. **Information Synthesis**: An AI chatbot utilizing RAG technology with access to both real-time market data and historical news can provide more contextual and actionable investment insights compared to traditional search or analysis tools.

2. **Visual Analytics**: Interactive visualization of portfolio performance, stock price trends, and sector distribution enables faster pattern recognition and better understanding of portfolio composition and risk exposure.

3. **Centralized Intelligence**: Consolidating multiple data sources (stock prices, news articles, company information) into a single interface reduces the time required for investment research and analysis by at least 50% compared to using multiple disparate tools.

4. **Accessibility**: A user-friendly web interface with natural language query capabilities democratizes access to sophisticated investment analysis, making it available to investors without technical or financial expertise.

## Data Description

### Data Sources

The Portfolio Intelligence Dashboard integrates data from multiple sources to provide comprehensive investment intelligence:

#### 1. Stock Market Data

**Source**: Alpha Vantage API
- **Type**: Time-series financial data
- **Frequency**: Daily updates
- **Coverage**: 18 stocks across multiple sectors (Technology, Finance, Services, Semiconductors, Quantum Computing)
- **Data Points**:
  - Daily open, close, high, low prices
  - Trading volume
  - Historical price data (6+ months)
- **Update Mechanism**: Automated script (`refresh_stock_prices.py`) that fetches and updates stock prices from Alpha Vantage API

**Portfolio Holdings**:
- **Quantum Computing**: QBTS, IONQ, QUBT, RGTI
- **Technology Giants**: META, MSFT, GOOGL, AMZN, ORCL, IBM
- **Semiconductors/AI**: NVDA, AMD, AVGO, ASML
- **Specialized**: PLTR (Data Analytics), FTNT (Cybersecurity), FN (Finance), FDS (Financial Data)

#### 2. Market News Data

**Source**: ActuallyFreeAPI (News API)
- **Type**: Financial news articles and market updates
- **Frequency**: Real-time collection, periodic bulk updates
- **Coverage**: General market news and company-specific news for portfolio stocks
- **Data Points**:
  - Article title and content
  - Publication timestamp
  - Source/publisher information
  - Relevance to specific stocks or sectors
- **Collection Method**: Bulk news collector script (`bulk_news_collector.py`) that fetches up to 1000 articles
- **Storage**: Articles are stored in PostgreSQL database and indexed in ChromaDB vector store for semantic search

#### 3. Company Information

**Type**: Static reference data
- Company names and stock symbols
- Sector classification
- Company logos and branding
- Portfolio metadata (addition dates, initial investment data)

### Data Storage and Processing

#### Database Architecture

**PostgreSQL Database**: Primary relational data store
- **Tables**:
  - `stocks`: Company information and portfolio holdings
  - `stock_prices`: Historical and current price data
  - `news_articles`: Collected news and market information
  - Portfolio transaction history

**ChromaDB Vector Store**: Semantic search and RAG support
- Embeddings of news articles for similarity search
- Enables natural language queries over historical news data
- Supports context retrieval for AI chatbot responses

### Data Processing Pipeline

1. **Ingestion**: Automated scripts fetch data from APIs on scheduled intervals
2. **Validation**: Data quality checks ensure consistency and completeness
3. **Storage**: Structured data stored in PostgreSQL, unstructured text in vector database
4. **Indexing**: News articles are embedded and indexed for semantic search
5. **Serving**: REST API endpoints provide data to frontend application

### Data Volume and Scale

- **Stock Data**: ~100 data points per stock per day × 18 stocks × 180+ days = 324,000+ price records
- **News Articles**: 1000+ articles with full content and metadata
- **Vector Embeddings**: Dense vector representations for each article enabling semantic search
- **Real-time Updates**: WebSocket connections for live data streaming

### Data Quality and Reliability

- **API Rate Limiting**: Respectful API usage with caching to prevent rate limit issues
- **Error Handling**: Graceful degradation when external APIs are unavailable
- **Data Validation**: Type checking and range validation for all incoming data
- **Backup Strategy**: Regular database backups to prevent data loss

## Technical Implementation

The application uses a modern full-stack architecture:
- **Frontend**: React with Vite, Recharts for visualization
- **Backend**: Python FastAPI with SQLAlchemy ORM
- **Database**: PostgreSQL for relational data, ChromaDB for vector search
- **Containerization**: Docker Compose for consistent deployment

### API Usage

The following external APIs are integrated into the application:

1. **Alpha Vantage API** - Stock market data and historical prices
2. **ActuallyFreeAPI** - Financial news articles and market updates
3. **Google Gemini API** - AI-powered text generation, embeddings, and natural language processing for the chatbot
4. **Finnhub API** - Additional market data (configured, available for use)
5. **Marketstack API** - Backup market data source (configured, available for use)
6. **Polygon API** - Alternative financial data provider (configured, available for use)

This data-rich foundation enables the Portfolio Intelligence Dashboard to provide actionable insights, contextual market analysis, and intelligent investment advisory capabilities to users.
