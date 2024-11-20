DRIVER_LICENSE_DATA_EXTRACTION_PROMPT = (
                        "Extract all available information from this driver's license image. "
                        "Include the following fields: state, license number, full name, date of birth, "
                        "expiration date, issue date, address, gender, height, weight, eye color, hair color, "
                        "endorsements, restrictions, and class type. If any field is missing or illegible, "
                        "return `None` for that field. Do not infer or guess missing data. "
                        "The response must strictly conform to the provided schema."
                    )

PASSPORT_DATA_EXTRACTION_PROMPT = (
                        "Extract all available information from this passport image. "
                        "Include the following fields: country, passport number, full name, date of birth, "
                        "expiration date, issue date, place of birth, nationality, and sex. "
                        "Make sure to extract all the required data. The response must strictly conform to the provided schema."
                    )