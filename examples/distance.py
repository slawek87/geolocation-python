# -*- coding: utf-8 -*-
from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

if __name__ == "__main__":
    origins = ['rybnik', 'oslo']
    destinations = ['zagrzeb']

    google_maps = GoogleMaps(api_key='your_google_maps_key')

    items = google_maps.distance(origins, destinations).all()  # default mode parameter is const.MODE_DRIVING

    for item in items:
        print('origin: %s' % item.origin)
        print('destination: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)
        print('m: %s' % item.distance.meters)
        print('miles: %s' % item.distance.miles)
        print('duration: %s' % item.duration)  # it returns str
        print('duration datetime: %s' % item.duration.datetime)  # it returns datetime

        # you can also get items from duration
        print('duration days: %s' % item.duration.days)
        print('duration hours: %s' % item.duration.hours)
        print('duration minutes: %s' % item.duration.minutes)
        print('duration seconds: %s' % item.duration.seconds)

    items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_BICYCLING).all()

    for item in items:
        print('origin: %s' % item.origin)
        print('destination: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)
        print('m: %s' % item.distance.meters)
        print('miles: %s' % item.distance.miles)
        print('duration: %s' % item.duration)

    items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_WALKING).all()

    for item in items:
        print('origin: %s' % item.origin)
        print('destination: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)
        print('m: %s' % item.distance.meters)
        print('miles: %s' % item.distance.miles)
        print('duration: %s' % item.duration)

    items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_TRANSIT).all()

    for item in items:
        print('origin: %s' % item.origin)
        print('destination: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)
        print('m: %s' % item.distance.meters)
        print('miles: %s' % item.distance.miles)
        print('duration: %s' % item.duration)

    items = google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_HIGHWAYS).all()

    for item in items:
        print('origin: %s' % item.origin)
        print('destination: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)
        print('m: %s' % item.distance.meters)
        print('miles: %s' % item.distance.miles)
        print('duration: %s' % item.duration)

    items = google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_FERRIES).all()

    for item in items:
        print('origin: %s' % item.origin)
        print('destination: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)
        print('m: %s' % item.distance.meters)
        print('miles: %s' % item.distance.miles)
        print('duration: %s' % item.duration)

    items = google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_TOLLS).all()

    for item in items:
        print('origin: %s' % item.origin)
        print('destination: %s' % item.destination)
        print('km: %s' % item.distance.kilometers)
        print('m: %s' % item.distance.meters)
        print('miles: %s' % item.distance.miles)
        print('duration: %s' % item.duration)
