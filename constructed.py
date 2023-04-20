import random

from fpdf import FPDF
from datetime import datetime, timedelta
from os import walk as oswalk
# import os

class PDF(FPDF):

    def logoImages(self, path):
        logoImages = []
        for root, dir, files in oswalk(f'{path}'):
            for file in files:
                logoImages.append(root + '/' + file)
        pro_img = random.choice(logoImages)

        return pro_img

    def xheader(self, vaddress, vphone, title):
        # Logo
        #self.image(str(self.logoImages(f"{os.path.dirname(os.path.realpath(__file__))}/images/")), 3, 5, 15)
        #self.image(str(self.logoImages(f"{os.getcwd()}/images/")), 3, 5, 15)
        #self.image("/usr/include/pxmailer/fox_face.png", 3, 5, 15)
        # font
        self.set_font('helvetica', 'BU', 15)
        # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        self.set_text_color(0, 80, 180)  # text = red
        # Thickness of frame (border)
        self.set_line_width(1)
        # Title
        self.cell(title_w, 10, title, border=0, ln=1, align='C', fill=0)
        # Line break
        # self.ln(10)
        self.set_text_color(0, 0, 0)
        # set font address
        self.set_font('times', '', 12)
        # insert address
        self.cell(0, 6, vaddress, ln=1, align='C')
        # set font phone
        self.set_font('times', '', 10)
        # insert phone
        self.cell(0, 6, vphone, ln=1, align='C')

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Set font color grey
        self.set_text_color(169,169,169)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    # Adding chapter title to start of each chapter
    def chapter_title(self, vname):
        # set font
        self.set_font('helvetica', 'BU', 12)
        # background color
        self.set_fill_color(200, 220, 255)
        self.ln()
        self.multi_cell(0, 5, f"{vname}\nTO WHOM IT MAY CONCERN", fill=0, align='C')
        # line break
        self.ln()

    # Chapter content
    def chapter_body(self, msg_gen):
        # read text file
        txt = msg_gen#.decode('latin-1')
        # set font
        self.set_font('times', '', 12)
        # insert text
        self.multi_cell(0, 5, txt)
        # line break
        self.ln()


    def print_chapter(self, link, name, position, corp, msg_gen, footer_gen, address_gen, phone_gen, vname):
        self.add_page()
        self.xheader(address_gen, phone_gen, corp)
        #add date
        self.set_font('times', '', 10)
        self.cell(0, 8, str(datetime.today()).split(" ")[0], ln=1, align='R')
        #title
        self.chapter_title(vname)
        # Add chapter
        #self.cell(0, 10, ' ', ln=1)
        self.chapter_body(msg_gen)
        # Attach Links
        self.set_right_margin(108)
        self.set_draw_color(0, 80, 180)  # border = blue
        self.set_fill_color(0, 80, 180)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'View Document', fill=1, border=1, ln=1, link=link)
        # # Chapter continue
        self.ln()
        self.set_text_color(0, 0, 0)
        self.set_right_margin(10)
        self.multi_cell(0, 5, f"If you are having difficulties try downloading the attachment or copying the below link to your web browser for more information.")
        self.set_text_color(0, 80, 180)
        self.multi_cell(0, 5, f"\n{link}\n")
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 10, f"{footer_gen}\nBest Regards\n")
        self.set_text_color(0, 80, 180)
        self.set_font('helvetica', '', 12)
        self.multi_cell(0, 5, name)
        self.set_font('helvetica', '', 10)
        self.multi_cell(0, 5, f"Phone: {phone_gen}")
        self.set_font('helvetica', '', 12)
        self.multi_cell(0, 5, position)
        self.set_font('helvetica', '', 10)
        self.multi_cell(0, 5, f"{corp.lower()}\n{address_gen.lower()}.")


