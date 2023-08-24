from bardapi import Bard, BardCookies


class BardAPIConsumer:

    def __init__(self, PSID: str, PSIDTS: str):
        self.PSID = PSID
        self.PSIDTS = PSIDTS
        cookie_dict = {
            "__Secure-1PSID": PSID,
            "__Secure-1PSIDTS": PSIDTS,
            # Any cookie values you want to pass session object.
        }
        self.bard = BardCookies(cookie_dict=cookie_dict)

    def get_report_text(self, queryString) -> str:
        report = self.bard.get_answer(queryString)['content']
        return report

    def export_word(self, reportText: str):
        from docx import Document
        from docx.shared import Pt, RGBColor
        value = reportText
        doc = Document()

        # Define styles for headings and paragraphs
        # 1 corresponds to paragraph style
        heading_style = doc.styles.add_style('HeadingStyle', 1)
        heading_font = heading_style.font
        heading_font.bold = True
        heading_font.size = Pt(16)
        heading_style.paragraph_format.alignment = 3  # Justify alignment
        heading_font.color.rgb = RGBColor(51, 51, 51)

        # 1 corresponds to paragraph style
        body_style = doc.styles.add_style('BodyStyle', 1)
        body_style.paragraph_format.alignment = 3  # Justify alignment

        # Process sections and add them to the document
        sections = value.split('**')
        for i in range(1, len(sections), 2):
            heading_text = sections[i].strip()
            content_text = sections[i + 1].strip()

            if heading_text and content_text:
                # Add heading
                heading = doc.add_paragraph(heading_text, style='HeadingStyle')

                # Add content with bullet points
                content_lines = content_text.split('\n')
                for line in content_lines:
                    if line.strip().startswith('* '):
                        bullet_item = doc.add_paragraph(
                            line.strip()[2:], style='BodyStyle').style = 'ListBullet'
                    else:
                        doc.add_paragraph(line.strip(), style='BodyStyle')

        # Save the document
        doc.save('report.docx')
        # pass

    def image_desc(self):
        pass

    def refresh_cookies(self, PSID, PSIDTS):
        self.PSID = PSID
        self.PSIDTS = PSIDTS


if __name__ == '__main__':
    PSID = ""
    PSIDTS = ""
    bard = BardAPIConsumer(PSID=PSID, PSIDTS=PSIDTS)
    print(bard.get_report_text("Hello"))
