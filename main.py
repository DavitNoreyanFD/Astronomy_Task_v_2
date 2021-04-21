"""
the script works functionally, the necessary attributes are taken and
placed in the attributes of the Stars class to avoid unwanted use of a lot of index
this is a basic module, there are basic functions including open_tsv, n_high_mag, create_result
"""
import const_and_inp
import datetime
import stars
import sort_module


def open_tsv(data_tsv, fov_ra: float, fov_dec: float, ra_user_input: float, dec_user_input: float) -> list:
    """
    in order not to load memory, the function checks if the star enters the field of view and then
    adds to array
    """
    fov_ra_min = ra_user_input - fov_ra / 2
    fov_ra_max = ra_user_input + fov_ra / 2
    fov_dec_min = dec_user_input - fov_dec / 2
    fov_dec_max = dec_user_input + fov_dec / 2
    with open(data_tsv) as fd:
        list_of_db = []
        for row in fd:
            list_row = row.split('\t')
            try:
                if fov_ra_min < float(list_row[const_and_inp.INDEX_RA]) < fov_ra_max and \
                        fov_dec_min < float(list_row[const_and_inp.INDEX_DEC]) < fov_dec_max:
                    list_of_db.append(
                        stars.Star(
                            int(list_row[const_and_inp.INDEX_ID]),
                            float(list_row[const_and_inp.INDEX_RA]),
                            float(list_row[const_and_inp.INDEX_DEC]),
                            float(list_row[const_and_inp.INDEX_MAG])
                        )
                    )
            except ValueError:
                pass

        return list_of_db


def n_high_mag(array: list, num: int) -> list:
    """
functions strips out num elements from array
    """
    if len(array) > num:
        return array[:num]
    else:
        return array


def my_key_mag(item):
    return item.mag


def my_key_dist(item):
    return item.distance


def create_result(star_array: list):
    """
the function is designed to create the final output as a .csv file,
the file name is the date and time of the current time
    """
    with open(f'{datetime.datetime.now()}.csv', 'w') as csv_temp:
        head = 'ID'.center(20) + ',' + \
               'RA'.center(20) + ',' + \
               'DEC'.center(20) + ',' + \
               'MAG'.center(20) + ',' + \
               'DISTANCE'.center(20) + '\n'
        csv_temp.write(head)
        for star in star_array:
            row = f'{star.id}'.center(20) + ',' + \
                  f'{star.ra}'.center(20) + ',' + \
                  f'{star.dec}'.center(20) + ',' + \
                  f'{star.mag}'.center(20) + ',' + \
                  f'{star.distance}'.center(20) + '\n'
            csv_temp.write(row)


if __name__ == '__main__':
    ob_list = open_tsv(const_and_inp.data_file,
                       const_and_inp.fov_v,
                       const_and_inp.fov_h,
                       const_and_inp.ra_user,
                       const_and_inp.dec_user)  # we get stars that come into view
    sorted_list_by_mag = sort_module.quicksort(ob_list, key=my_key_mag)  # we sort stars by brightness
    ob_list_n_high = n_high_mag(sorted_list_by_mag, const_and_inp.n)  # we take N number of stars
    sorted_list_by_dist = sort_module.quicksort(ob_list_n_high, key=my_key_dist)  # we sort stars by distance
    create_result(sorted_list_by_dist)  # create output result
