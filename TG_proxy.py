i = 0
with open("Long_term_subscription_num", "w", encoding="utf-8") as file:
    for code in processed_codes:
        if i == 0:
            config_string = "#🌐 Updated on " + final_string + ":00 | @config_kharaki"
        else:
            config_string = "#✅ " + str(final_string) + ":00-" + str(i)
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
