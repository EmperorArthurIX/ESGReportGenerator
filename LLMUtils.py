from bardapi import Bard, BardCookies


class BardAPIConsumer:

    def __init__(self, PSID: str, PSIDTS: str):
        self.PSID = PSID
        self.PSIDTS = PSIDTS
        self.bard = Bard()
        cookie_dict = {
            "__Secure-1PSID": PSID,
            "__Secure-1PSIDTS": PSIDTS,
            # Any cookie values you want to pass session object.
        }
        model = BardCookies(cookie_dict=cookie_dict)

    def get_report_text(self, queryString) -> str:
        report = self.bard.get_answer(queryString)
        return report

    def export_word(self, reportText: str):
        pass

    def image_desc(self):
        pass


if __name__ == '__main__':
    PSID = ""
    PSIDTS = ""
    bard = BardAPIConsumer(PSID=PSID, PSIDTS=PSIDTS)
    print(bard.get_report_text("Hello"))
