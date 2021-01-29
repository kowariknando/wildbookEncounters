class Locators():

    # login page objects
    username_textbox_name = "username"
    password_textbox_name = "password"
    login_button_id = "logMeIn"

    # searchEncounter page objects
    ## location filter map
    ne_lat_textbox_id = "ne_lat"
    ne_long_textbox_id = "ne_long"
    sw_lat_textbox_id = "sw_lat"
    sw_long_textbox_id = "sw_long"
    load_markers_button_xpath = "//*[@id='map_overlay_buttons']/input"
    ## location_filter_text
    location_filter_text_button_xpath = "// *[ @ id = 'search'] / table / tbody / tr[2] / td / h4 / a"
    location_filter_text_locationid_id = "locationCodeField"
    ## submit search
    search_button_id = "submitSearch"

    ##Encounter has pictures or no
    image_css = ".image-enhancer-wrapper"