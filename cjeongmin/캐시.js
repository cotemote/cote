const CACHE_HIT = 1;
const CACHE_MISS = 5;

function updateCache(cache, city, cacheSize) {
    if (cache.has(city)) {
        cache.delete(city);
        cache.set(city, true);
        return CACHE_HIT;
    }

    if (cacheSize > 0) {
        if (cache.size >= cacheSize) {
            const firstKey = cache.keys().next().value;
            cache.delete(firstKey);
        }
        cache.set(city, true);
    }
    return CACHE_MISS;
}

function solution(cacheSize, cities) {
    const cache = new Map();

    return cities
        .map((city) => city.toLowerCase())
        .reduce((totalTime, city) => totalTime + updateCache(cache, city, cacheSize), 0);
}
