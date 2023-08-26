from bardapi import BardCookies
import streamlit as st

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
                heading = doc.add_paragraph(heading_text, style='Heading Style')

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

    def image_desc(_self):
        pass

    def get_viz_data(_self):
        response = _self.bard.get_answer('''Please generate a semicolon-separated string of values showing Starbucks ESG data in the following manner:
"""year; greenhouse emissions (units); water usage (units); waste production (units)
<year1>; <int(value1)>; <int(value1)>; <int(value1)>
<year2>; <int(value2)>; <int(value2)>; <int(value2)>
"""
from 2018 to 2023''')
        return response['content']

    def refresh_cookies(_self, PSID, PSIDTS):
        _self.PSID = PSID
        _self.PSIDTS = PSIDTS
        cookie_dict = {
            "__Secure-1PSID": PSID,
            "__Secure-1PSIDTS": PSIDTS,
            # Any cookie values you want to pass session object.
        }
        _self.bard = BardCookies(cookie_dict=cookie_dict)


if __name__ == '__main__':
    PSID = ""
    PSIDTS = ""
    bard = BardAPIConsumer(PSID=PSID, PSIDTS=PSIDTS)
    print(bard.get_report_text("Hello"))
