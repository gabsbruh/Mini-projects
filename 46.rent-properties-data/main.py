import constants as c
from fill_form import FillForm
from get_properties import GetProperties
from property_data import Property_

def main():
    get_prop = GetProperties()
    properties_raw = get_prop.get_all_properties()
    
    # retrieve data about property from raw html content
    properties_data = []
    for property_ in properties_raw:
        properties_data.append(get_prop.get_info_about_property(property_))
    del get_prop
    
    fill_form = FillForm()
    for property_ in properties_data:
        fill_form.fill_out_form(property_)

if __name__ == "__main__":
    main()