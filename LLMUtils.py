from bardapi import BardCookies
import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt


class BardAPIConsumer:

    def __init__(_self, PSID: str, PSIDTS: str):
        _self.PSID = PSID
        _self.PSIDTS = PSIDTS
        cookie_dict = {
            "__Secure-1PSID": PSID,
            "__Secure-1PSIDTS": PSIDTS,
            # Any cookie values you want to pass session object.
        }
        _self.bard = BardCookies(cookie_dict=cookie_dict)

    @st.cache_resource()
    def get_report_text(_self, queryString) -> str:
        report = _self.bard.get_answer(queryString)['content']
        return report

    def export_word(_self, reportText: str):
        from docx import Document
        from docx.shared import Pt, RGBColor
        import io
        bio = io.BytesIO()
        value = reportText
        doc = Document()

        # Define styles for headings and paragraphs
        # 1 corresponds to paragraph style
        heading_style = doc.styles.add_style('Heading Style', 1)
        heading_font = heading_style.font
        heading_font.bold = True
        heading_font.size = Pt(16)
        heading_style.paragraph_format.alignment = 3  # Justify alignment
        heading_font.color.rgb = RGBColor(51, 51, 51)

        # 1 corresponds to paragraph style
        body_style = doc.styles.add_style('Body Style', 1)
        body_style.paragraph_format.alignment = 3  # Justify alignment

        # Process sections and add them to the document
        sections = value.split('**')
        for i in range(1, len(sections), 2):
            heading_text = sections[i].strip()
            content_text = sections[i + 1].strip()

            if heading_text and content_text:
                # Add heading
                heading = doc.add_paragraph(
                    heading_text, style='Heading Style')

                # Add content with bullet points
                content_lines = content_text.split('\n')
                for line in content_lines:
                    if line.strip().startswith('* '):
                        bullet_item = doc.add_paragraph(
                            line.strip()[2:], style='Body Style').style = 'List Bullet'
                    else:
                        doc.add_paragraph(line.strip(), style='Body Style')

        # Save the document
        doc.save(bio)
        return bio
        # pass

    def image_desc(_self, img_bio):
        # image = open('image_path', 'rb').read()
        # res = _self.bard.ask_about_image('Generate a python dictionary from the content of the image', image)['content']
        # return res
        # import io
        # img_bio = io.BytesIO()
        # img_bio.write(img_bio.read())
        # img_bio.seek(0)
        # res = _self.bard.ask_about_image(
            # 'Generate a python dictionary from the content of the image', image)['content']
        # return res
        pass

    def refresh_cookies(_self, PSID, PSIDTS):
        _self.PSID = PSID
        _self.PSIDTS = PSIDTS
        cookie_dict = {
            "__Secure-1PSID": PSID, -
            "__Secure-1PSIDTS": PSIDTS,
            # Any cookie values you want to pass session object.
        }
        _self.bard = BardCookies(cookie_dict=cookie_dict)

    #  Function Creating CSV Data
    # @st.cache_resource()
    def create_csv(_self, orgQuery, startYear, endYear):
        query = '''Please generate a csv report showing {} ESG data in the following manner:
                                    """year;greenhouse_emissions(units);water_usage(units);waste_production(units)
                                        <year1>;<int(value1)>;<int(value1)>;<int(value1)> 
                                        <year2>;<int(value2)>;<int(value2)>;<int(value2)>
                                        """from {} to {}'''
        res = _self.bard.get_answer(query.format(
            orgQuery, startYear, endYear))['code']
        with open("response.csv", "w+") as file:
            file.write(res)
            # print("CSV Response File Generated")
        return res

    # @st.cache_resource()
    def create_html(_self, orgQuery, startYear, endYear):
        query = '''Please generate a html report showing {} ESG data in the following strictly this manner:
                                    """year;greenhouse_emissions(units);water_usage(units);waste_production(units)
                                        <year1>;<int(value1)>;<int(value1)>;<int(value1)> 
                                        <year2>;<int(value2)>;<int(value2)>;<int(value2)>
                                        """from {} to {}'''
        res_html = _self.bard.get_answer(query.format(
            orgQuery, startYear, endYear))['code']

        with open("response.html", "w+") as file:
            file.write(res_html)
            # print("HTML Response File Generated")
        return res_html

    # Function Creating Plot on CSV Data; Headers to be provided
    def create_plot_html(_self, data):
        # import html data to pandas and create a bar plot
        # import pandas as pd
        # since read_html returns a list, we convert to a DataFrame
        df = pd.DataFrame(pd.read_html(data)[0])
        y_axis = list()
        for val in df.iloc[:, 1:]:
            # y = val.replace(" ", "_")
            y_axis.append(val)

        # Plotting
        # Fix a way to automatically get the X & Y - Axis List
        df.plot.bar(x='Year', y=y_axis, rot=0)
        # return plot
        # pass

    def create_plot_csv(_self, data):
        # import csv data to pandas and create a bar plot
        # import pandas as pd
        # import matplotlib.pyplot as plt
        df = pd.DataFrame(pd.read_csv(data, sep=","))

        # Plotting
        y_axis = list()
        for val in df.iloc[:, 1:]:
            # y = val.replace(" ", "_")
            y_axis.append(val)

        # Fix a way to automatically get the X & Y - Axis List
        df.plot.bar(x='year', y=y_axis, rot=0)

        # return plot
        # pass


if __name__ == '__main__':
    PSID = ""
    PSIDTS = ""
    bard = BardAPIConsumer(PSID=PSID, PSIDTS=PSIDTS)
    print(bard.get_report_text("Hello"))
