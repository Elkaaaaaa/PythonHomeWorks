def xml_export(data_set, file_name):
    xml = '<xml>\n'
    for data in data_set:
        id, familie, name, phones, description = data
        xml += '   <!--alias-->\n'
        xml += '   <_i_>{}</_i_>\n'.format(id)
        xml += '   <_f_>{}</_f_>\n'.format(familie)
        xml += '   <_n_>{}</_n_>\n'.format(name)
        for phone in phones:
            xml += '   <_p_>{}</_p_>\n'.format(phone)
        xml += '   <_d_>{}</_d_>\n'.format(description)
    xml += '</xml>'

    with open(file_name, "w") as file:
        file.write(xml)
    return xml


def html_export(data_set, file_name):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    for data in data_set:
        id, familie, name, phones, description = data
        html += '   <!--alias-->\n'
        html += '   <p>_i_:{}</p>\n'.format(id)
        html += '   <p>_f_:{}</p>\n'.format(familie)
        html += '   <p>_n_:{}</p>\n'.format(name)
        for phone in phones:
            html += '   <p>_p_:{}</p>\n'.format(phone)
        html += '   <p>_d_:{}</p>\n'.format(description)
    html += '   </body>\n</html>'

    with open(file_name, "w") as file:
        file.write(html)
    return html


def xml_import(file_name):
    useful_data = ["_i_", "_f_", "_n_", "_p_", "_d_"]
    id = ""
    familie = ""
    name = ""
    phones = []
    description = ""
    with open(file_name, "r") as file:
        data_set = []
        lines = file.readlines()
        for i in range(len(lines)):
            if "<!--alias-->" in lines[i]:
                phones = []
                j = 0
                endless_loop = 1
                while endless_loop:
                    line = lines[i + j + 1]
                    for usefull_sign in useful_data:
                        if usefull_sign in line:
                            line = line.replace(f"   <{usefull_sign}>", "")
                            line = line.replace(f"</{usefull_sign}>\n", "")
                            if usefull_sign == "_i_":
                                id = line
                            if usefull_sign == "_f_":
                                familie = line
                            if usefull_sign == "_n_":
                                name = line
                            if usefull_sign == "_p_":
                                phones.append(line)
                            if usefull_sign == "_d_":
                                description = line
                                endless_loop = 0
                    j += 1
                data_set.append((id, (familie, name, phones, description)))
    return data_set


def html_import(file_name):
    usefull_data = ["_i_", "_f_", "_n_", "_p_", "_d_"]
    id = ""
    familie = ""
    name = ""
    phones = []
    description = ""
    with open(file_name, "r") as file:
        data_set = []
        lines = file.readlines()
        for i in range(len(lines)):
            if "<!--alias-->" in lines[i]:
                phones = []
                j = 0
                endless_loop = 1
                while endless_loop:
                    line = lines[i + j + 1]
                    for usefull_sign in usefull_data:
                        if usefull_sign in line:
                            line = line.replace(f"   <p>{usefull_sign}:", "")
                            line = line.replace(f"</p>\n", "")
                            if usefull_sign == "_i_":
                                id = line
                            if usefull_sign == "_f_":
                                familie = line
                            if usefull_sign == "_n_":
                                name = line
                            if usefull_sign == "_p_":
                                phones.append(line)
                            if usefull_sign == "_d_":
                                description = line
                                endless_loop = 0
                    j += 1
                data_set.append((id, (familie, name, phones, description)))
    return data_set
