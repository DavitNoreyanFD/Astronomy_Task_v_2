import configparser
import datetime
import stars
import sort_module

config = configparser.ConfigParser()
config.read('config.ini')

data_file = config['USER']['datafile']
fov_v = float(config['USER']['fov_v'])
fov_h = float(config['USER']['fov_h'])
ra_user = float(config['USER']['ra_user'])
dec_user = float(config['USER']['dec_user'])
n = int(config['USER']['n'])

INDEX_ID = 7
INDEX_RA = 0
INDEX_DEC = 1
INDEX_MAG = 22
INDEX_FLUX = 20


def open_tsv(data_tsv, fov_ra, fov_dec, ra_user_input, dec_user_input) -> list:
    """
    in order not to load memory, the function checks if the star enters the field of view and then
    adds to array
    :param data_tsv:
    :param fov_ra:
    :param fov_dec:
    :param ra_user_input:
    :param dec_user_input:
    :return:
    """
    with open(data_tsv) as fd:
        list_of_db = []
        next(fd)
        for row in fd:
            list_row = row[:-1].split('\t')
            try:

                if (ra_user_input - fov_ra / 2) < float(
                        list_row[INDEX_RA]) < (ra_user_input + fov_ra / 2) and (dec_user_input - fov_dec / 2) < float(
                        list_row[INDEX_DEC]) < (dec_user_input + fov_dec / 2):
                    list_of_db.append(
                        stars.Star(
                            int(list_row[INDEX_ID]),
                            float(list_row[INDEX_RA]),
                            float(list_row[INDEX_DEC]),
                            float(list_row[INDEX_MAG]),
                            float(list_row[INDEX_FLUX])
                        )
                    )
            except ValueError:
                pass
        return list_of_db


def n_high_mag(array, count):
    if len(array) > count:
        return array[:count]
    else:
        return array


def my_key(item):
    return item.mag


def create_result(star_array):
    with open(f'{datetime.datetime.now()}.csv', 'w') as csv_temp:
        csv_temp.write('id \t ra\t dec\t mag\t flux \t distance \n')
        for star in star_array:
            csv_temp.write(f'{star.id},{star.ra},{star.dec},{star.mag},{star.flux},{star.distance}\n')


ob_list = open_tsv(data_file, fov_v, fov_h, ra_user, dec_user)
sorted_list = sort_module.quicksort(ob_list, key=my_key)
create_result(sorted_list)


