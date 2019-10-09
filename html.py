import csv


def str_to_list(text):
    text = text.strip('[').strip(']').replace('\'', '').strip()
    # print(text)
    text_list = text.split(',')
    return text_list


def gen_html_table(text_dict):
    header_body = """
    <tr>
        <th>brand</th>
        <th>city</th>
        <th>number</th>
        <th>centers</th>
    </tr>
    """

    content_body = ""

    city_count = {'ef': 0, 'meteni': 0, 'webi': 0, 'wse': 0}

    for i in range(0, len(text_dict['city'])):
        if text_dict['brand'][i] == 'ef':
            city_count['ef'] = city_count['ef'] + 1
        elif text_dict['brand'][i] == 'meteni':
            city_count['meteni'] = city_count['meteni'] + 1
        elif text_dict['brand'][i] == 'webi':
            city_count['webi'] = city_count['webi'] + 1
        elif text_dict['brand'][i] == 'wse':
            city_count['wse'] = city_count['wse'] + 1

    print(city_count)

    for i in range(0, len(text_dict['city'])):
        centers_body = ""

        for j in range(0, len(text_dict['centers'][i])):
            centers_body = centers_body + """
                <td>
                    {}
                </td>
                """.format(text_dict['centers'][i][j])

        content_body = content_body + """
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            {}
        </tr>
        """.format(text_dict['brand'][i], text_dict['city'][i], text_dict['number'][i], centers_body)

    table_body = """
    <table border="1" class="dataframe" style="text-align: center;">
        <thead>
            {}
         </thead>
         <tbody>
            {}
         </tbody>
    </table>
    """.format(header_body, content_body)

    return table_body


if __name__ == '__main__':
    with open('school_number_2019-05-21.csv') as fp:
        reader = csv.reader(fp)

        brand = []
        city = []
        number = []
        centers = []

        for line in reader:
            # print(line)
            brand.append(line[1])
            city.append(line[2])
            number.append(line[3])

            center_list = str_to_list(line[4])
            centers.append(center_list)

        fp.close()

        print(brand)
        print(city)
        print(number)
        print(centers)

        content = {'brand': brand, 'city': city, 'number': number, 'centers': centers}
        html_body = gen_html_table(content)

        with open('school_number.html', 'w') as fc:
            fc.write(html_body)
            fc.close()
