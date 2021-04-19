# Elastic stack

Formerly known as ELK stack (Elastic, , Kibana)

- Elasticsearch: storage, search and analytics engine
- Logstash: log transformation 
- Kibana: analytics and visualization platform

## Elasticsearch

### Installation

- Download from [downloads page](https://www.elastic.co/de/downloads/elasticsearch)
- Unpack to arbitrary directory
- Execute `bin\elasticsearch.bat`
- Go to `http://127.0.0.1:9200` 

### Usage

curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'


## Kibana

### Installation

- Download from [downloads page](https://www.elastic.co/de/downloads/elasticsearch)
- Unpack to arbitrary directory
- Execute `bin\kibana.bat`
- Go to `http://127.0.0.1:5601` 

# XML Test results

See [Stack Overflow Answer](https://stackoverflow.com/questions/50518450/xunit-test-results-to-elk-stack-anyone-tried-this-or-know-of-projects):
Convert XML to JSON and pot to elastic

[Medium Article](https://medium.com/@akritichanana13/post-junit-test-results-to-elastic-3b73d094711c): Use junitparser and requests to post data


## Scratch

- Test reporting: https://discuss.elastic.co/t/visualization-for-automation-test-reporting/181074
https://experitest.com/mobile-app-testing/how-a-big-data-tool-like-elasticsearch-will-shorten-your-test-result-analysis/
- https://apifortress.com/send-api-test-results-to-elastic-and-visualize-in-kibana/
https://tech.trivago.com/2015/12/02/selenium_with_kibana/
https://postmarkapp.com/blog/migration-to-elasticsearch-through-the-eyes-of-qa
http://vikasthange.blogspot.com/2018/01/elasticsearch-and-kibana-for-test.html