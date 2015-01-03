# -*- coding: utf-8 -*-
from geolocation.google_maps import GoogleMaps
from geolocation.distance_matrix import const

if __name__ == "__main__":
    origins = ['rybnik', 'oslo']
    destinations = ['zagrzeb']

    google_maps = GoogleMaps(api_key='your_google_maps_key')

    items = google_maps.distance(origins, destinations).all()

    for item in items:
        print 'origin: %s' % item.origin
        print 'destination: %s' % item.destination
        print 'km: %s' % item.distance.kilometers
        print 'm: %s' % item.distance.meters
        print 'miles: %s' % item.distance.miles
        print 'duration: %s' % item.duration

    items = google_maps.distance(origins, destinations).all()

    for item in items:
        print 'origin: %s' % item.origin
        print 'destination: %s' % item.destination
        print 'km: %s' % item.distance.kilometers
        print 'm: %s' % item.distance.meters
        print 'miles: %s' % item.distance.miles
        print 'duration: %s' % item.duration

    items = google_maps.distance(origins, destinations, const.MODE_BICYCLING).all()

    for item in items:
        print 'origin: %s' % item.origin
        print 'destination: %s' % item.destination
        print 'km: %s' % item.distance.kilometers
        print 'm: %s' % item.distance.meters
        print 'miles: %s' % item.distance.miles
        print 'duration: %s' % item.duration

    items = google_maps.distance(origins, destinations, const.MODE_WALKING).all()

    for item in items:
        print 'origin: %s' % item.origin
        print 'destination: %s' % item.destination
        print 'km: %s' % item.distance.kilometers
        print 'm: %s' % item.distance.meters
        print 'miles: %s' % item.distance.miles
        print 'duration: %s' % item.duration

    items = google_maps.distance(origins, destinations, avoid=const.AVOID_HIGHWAYS).all()

    for item in items:
        print 'origin: %s' % item.origin
        print 'destination: %s' % item.destination
        print 'km: %s' % item.distance.kilometers
        print 'm: %s' % item.distance.meters
        print 'miles: %s' % item.distance.miles
        print 'duration: %s' % item.duration

    items = google_maps.distance(origins, destinations, avoid=const.AVOID_FERRIES).all()

    for item in items:
        print 'origin: %s' % item.origin
        print 'destination: %s' % item.destination
        print 'km: %s' % item.distance.kilometers
        print 'm: %s' % item.distance.meters
        print 'miles: %s' % item.distance.miles
        print 'duration: %s' % item.duration

    items = google_maps.distance(origins, destinations, avoid=const.AVOID_TOLLS).all()

    for item in items:
        print 'origin: %s' % item.origin
        print 'destination: %s' % item.destination
        print 'km: %s' % item.distance.kilometers
        print 'm: %s' % item.distance.meters
        print 'miles: %s' % item.distance.miles
        print 'duration: %s' % item.duration