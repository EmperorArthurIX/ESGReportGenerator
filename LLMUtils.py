from bardapi import Bard

class BardAPIConsumer:

    def __init__(self, PSID: str, PSIDTS: str):
        self.PSID = PSID
        self.PSIDTS = PSIDTS
        self.bard = Bard()
    
    def get_report_text(self, queryString) -> str:
        report = self.bard.get_answer(queryString)
        return report
    
    def export_word(self, reportText: str):
        pass
    

if __name__ == '__main__':
    PSID = ""
    PSIDTS = ""
    bard = BardAPIConsumer(PSID=PSID, PSIDTS=PSIDTS)
    print(bard.get_report_text("Hello"))