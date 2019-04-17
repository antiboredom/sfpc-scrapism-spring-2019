SELECT DISTINCT ?cityLabel ?population ?gps
WHERE
{
  ?city wdt:P31/wdt:P279* wd:Q515 .
  ?city wdt:P1082 ?population .
  ?city wdt:P625 ?gps .
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY DESC(?population) LIMIT 10000

=> View as table
=> remove duplicates, they mess up the counts when we graph
sort -n -t: -k2 query.tsv | sort -u -k1,1 | sort -k2 -n | tail -r > top_cities.txt
