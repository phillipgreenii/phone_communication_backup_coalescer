'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Phillip Green II
Licensed under MIT
'''

import unittest

import tree_support
from phone_communication_backup_coalescer.sms import SmsBackupControl, SMS, MMS, MMSPart, MMSAddress
from phone_communication_backup_coalescer.utils import ParseSupport


class SmsParseFileTestCase(unittest.TestCase, tree_support.BuildTreeAssertions):
    def setUp(self):
        self.backup_control = SmsBackupControl(ParseSupport())

    def test_build_tree_with_no_smses(self):
        smses = []
        expected_string = '<smses count="0" />'

        tree = self.backup_control.build_tree(smses)

        self.assert_tree_as_string(tree, expected_string)

    def test_build_tree_with_simple_smses(self):
        smses = [
            SMS(
                body='This is Phillip',
                service_center='null',
                protocol='0',
                read='1', sc_toa='null',
                readable_date='Jul 15, 2013 10:41:45 PM',
                date_sent='0',
                status='-1',
                address='+15555550000',
                date='1373942505322',
                locked='0',
                contact_name='Jane Smith',
                toa='null',
                type='2',
                subject='null'),
            SMS(
                body='Free AT&T msg: Your Authorized user was changed for acct # ending in XXXX. If this was done in error, call 800-331-0500 or 611 from your wireless phone.',
                service_center='+13123149623',
                protocol='0',
                read='1',
                sc_toa='null',
                readable_date='Jul 15, 2013 7:12:55 PM',
                date_sent='1373929975000',
                status='-1',
                address='7535',
                date='1373929975000',
                locked='0',
                contact_name='(Unknown)',
                toa='null',
                type='1',
                subject='null')]
        expected_string = '<smses count="2">' + \
                          '<sms address="+15555550000" body="This is Phillip" contact_name="Jane Smith" date="1373942505322" date_sent="0" locked="0" protocol="0" read="1" readable_date="Jul 15, 2013 10:41:45 PM" sc_toa="null" service_center="null" status="-1" subject="null" toa="null" type="2" />' + \
                          '<sms address="7535" body="Free AT&amp;T msg: Your Authorized user was changed for acct # ending in XXXX. If this was done in error, call 800-331-0500 or 611 from your wireless phone." contact_name="(Unknown)" date="1373929975000" date_sent="1373929975000" locked="0" protocol="0" read="1" readable_date="Jul 15, 2013 7:12:55 PM" sc_toa="null" service_center="+13123149623" status="-1" subject="null" toa="null" type="1" />' + \
                          '</smses>'

        tree = self.backup_control.build_tree(smses)

        self.assert_tree_as_string(tree, expected_string)

    def test_build_tree_with_simple_mms(self):
        smses = [
            MMS(
                callback_set='0',
                m_id='103019290470004800008',
                reserved='0',
                creator=None,
                msg_id='0',
                pri='129',
                app_id='0',
                retr_txt='null',
                sub_cs='null',
                seen='1',
                contact_name='Ted Turner',
                sub='',
                rr='129',
                text_only='1',
                ct_t='application/vnd.wap.multipart.related',
                ct_l='null',
                m_size='6',
                resp_st='128',
                msg_box='2',
                readable_date='Oct 30, 2014 3:29:04 PM',
                rpt_a='null',
                read='1',
                retr_txt_cs='null',
                d_rpt='129',
                spam_report=None,
                deletable='0',
                address='+15555550001',
                date='1414697344000',
                sim_slot=None,
                sim_imsi=None,
                hidden='0',
                resp_txt='null',
                ct_cls='null',
                tr_id='T14962885023',
                locked='0',
                m_type='128',
                sub_id=None,
                retr_st='null',
                safe_message=None,
                d_tm='null',
                st='null',
                m_cls='personal',
                exp='604800',
                v='18',
                date_sent='0',
                read_status='null',
                parts=(
                    MMSPart(
                        name='null',
                        seq='-1',
                        cl='smil.xml',
                        text='<smil><head><layout><root-layout width="100px" height="1080px"/><region id="Text" left="0" top="972" width="100px" height="108px" fit="meet"/></layout></head><body><par dur="5000ms"><text src="cid:text_0.txt" region="Text"/></par></body></smil>',
                        cid='<smil>',
                        chset='null',
                        cd='null',
                        ctt_t='null',
                        ctt_s='null',
                        data=None,
                        fn='null',
                        ct='application/smil'),
                    MMSPart(
                        name='null',
                        seq='0',
                        cl='text_0.txt',
                        text="I'm in",
                        cid='<text_0.txt>',
                        chset='106',
                        cd='null',
                        ctt_t='null',
                        ctt_s='null',
                        data=None,
                        fn='null',
                        ct='text/plain')),
                addresses=())]
        expected_string = '' + \
            '<smses count="1">' + \
            '<mms address="+15555550001" app_id="0" callback_set="0" contact_name="Ted Turner" ct_cls="null" ct_l="null" ct_t="application/vnd.wap.multipart.related" d_rpt="129" d_tm="null" date="1414697344000" date_sent="0" deletable="0" exp="604800" hidden="0" locked="0" m_cls="personal" m_id="103019290470004800008" m_size="6" m_type="128" msg_box="2" msg_id="0" pri="129" read="1" read_status="null" readable_date="Oct 30, 2014 3:29:04 PM" reserved="0" resp_st="128" resp_txt="null" retr_st="null" retr_txt="null" retr_txt_cs="null" rpt_a="null" rr="129" seen="1" st="null" sub="" sub_cs="null" text_only="1" tr_id="T14962885023" v="18">' + \
            '<parts>' + \
            '<part cd="null" chset="null" cid="&lt;smil&gt;" cl="smil.xml" ct="application/smil" ctt_s="null" ctt_t="null" fn="null" name="null" seq="-1" text="&lt;smil&gt;&lt;head&gt;&lt;layout&gt;&lt;root-layout width=&quot;100px&quot; height=&quot;1080px&quot;/&gt;&lt;region id=&quot;Text&quot; left=&quot;0&quot; top=&quot;972&quot; width=&quot;100px&quot; height=&quot;108px&quot; fit=&quot;meet&quot;/&gt;&lt;/layout&gt;&lt;/head&gt;&lt;body&gt;&lt;par dur=&quot;5000ms&quot;&gt;&lt;text src=&quot;cid:text_0.txt&quot; region=&quot;Text&quot;/&gt;&lt;/par&gt;&lt;/body&gt;&lt;/smil&gt;" />' + \
            '<part cd="null" chset="106" cid="&lt;text_0.txt&gt;" cl="text_0.txt" ct="text/plain" ctt_s="null" ctt_t="null" fn="null" name="null" seq="0" text="I\'m in" />' + \
            '</parts>' + \
            '<addresses />' + \
            '</mms>' + \
            '</smses>'

        tree = self.backup_control.build_tree(smses)

        self.assert_tree_as_string(tree, expected_string)

    def test_build_tree_with_mms_with_image(self):
        smses = [
            MMS(
                callback_set='0',
                m_id='110213558440201660001',
                reserved='0',
                creator=None,
                msg_id='0',
                pri='129',
                app_id='0',
                retr_txt='null',
                sub_cs='null',
                seen='1',
                contact_name='Jane Smith',
                sub='',
                rr='129',
                text_only='0',
                ct_t='application/vnd.wap.multipart.related',
                ct_l='null',
                m_size='955312',
                resp_st='128',
                msg_box='2',
                readable_date='Nov 2, 2014 8:55:28 AM',
                rpt_a='null',
                read='1',
                retr_txt_cs='null',
                d_rpt='129',
                spam_report=None,
                deletable='0',
                address='+15555550000',
                date='1414936528000',
                sim_slot=None,
                sim_imsi=None,
                hidden='0',
                resp_txt='null',
                ct_cls='null',
                tr_id='T14170c8f96c',
                locked='0',
                m_type='128',
                sub_id=None,
                retr_st='null',
                safe_message=None,
                d_tm='null',
                st='null',
                m_cls='personal',
                exp='604800',
                v='18',
                date_sent='0',
                read_status='null',
                parts=(
                    MMSPart(
                        name='null',
                        seq='-1',
                        cl='smil.xml',
                        text='<smil><head><layout><root-layout width="100px" height="100px"/><region id="Image" left="0" top="0" width="100px" height="100px" fit="meet"/></layout></head><body><par dur="5000ms"><img src="duck.png" region="Image"/></par></body></smil>',
                        cid='<smil>',
                        chset='null',
                        cd='null',
                        ctt_t='null',
                        ctt_s='null',
                        data=None,
                        fn='null',
                        ct='application/smil'),
                    MMSPart(
                        name='null',
                        seq='0',
                        cl='duck.png',
                        text='null',
                        cid='<duck>',
                        chset='null',
                        cd='null',
                        ctt_t='null',
                        ctt_s='null',
                        data='abcd1234',
                        fn='duck.png',
                        ct='image/png')),
                addresses=())]
        expected_string = '' + \
            '<smses count="1">' + \
            '<mms address="+15555550000" app_id="0" callback_set="0" contact_name="Jane Smith" ct_cls="null" ct_l="null" ct_t="application/vnd.wap.multipart.related" d_rpt="129" d_tm="null" date="1414936528000" date_sent="0" deletable="0" exp="604800" hidden="0" locked="0" m_cls="personal" m_id="110213558440201660001" m_size="955312" m_type="128" msg_box="2" msg_id="0" pri="129" read="1" read_status="null" readable_date="Nov 2, 2014 8:55:28 AM" reserved="0" resp_st="128" resp_txt="null" retr_st="null" retr_txt="null" retr_txt_cs="null" rpt_a="null" rr="129" seen="1" st="null" sub="" sub_cs="null" text_only="0" tr_id="T14170c8f96c" v="18">' + \
            '<parts>' + \
            '<part cd="null" chset="null" cid="&lt;smil&gt;" cl="smil.xml" ct="application/smil" ctt_s="null" ctt_t="null" fn="null" name="null" seq="-1" text="&lt;smil&gt;&lt;head&gt;&lt;layout&gt;&lt;root-layout width=&quot;100px&quot; height=&quot;100px&quot;/&gt;&lt;region id=&quot;Image&quot; left=&quot;0&quot; top=&quot;0&quot; width=&quot;100px&quot; height=&quot;100px&quot; fit=&quot;meet&quot;/&gt;&lt;/layout&gt;&lt;/head&gt;&lt;body&gt;&lt;par dur=&quot;5000ms&quot;&gt;&lt;img src=&quot;duck.png&quot; region=&quot;Image&quot;/&gt;&lt;/par&gt;&lt;/body&gt;&lt;/smil&gt;" />' + \
            '<part cd="null" chset="null" cid="&lt;duck&gt;" cl="duck.png" ct="image/png" ctt_s="null" ctt_t="null" data="abcd1234" fn="duck.png" name="null" seq="0" text="null" />' + \
            '</parts>' + \
            '<addresses />' + \
            '</mms>' + \
            '</smses>'

        tree = self.backup_control.build_tree(smses)

        self.assert_tree_as_string(tree, expected_string)

    def test_build_tree_with_mms_with_multiple_addresses(self):
        smses = [
            MMS(
                callback_set='0',
                m_id='479E1FAE-E4A4-71F4-7B68-A8D385BCA5DE',
                reserved='0',
                creator='null',
                msg_id='0',
                pri='129',
                app_id='0',
                retr_txt='null',
                sub_cs='null',
                seen='0',
                contact_name='Ted Turner, Nancy Edgar, Antonio Scott, Max Hall',
                sub='null',
                rr='null',
                text_only='1',
                ct_t='application/vnd.wap.multipart.related',
                ct_l='null',
                m_size='318',
                resp_st='null',
                msg_box='1',
                readable_date='Apr 16, 2015 9:51:40 PM',
                rpt_a='null',
                read='1',
                retr_txt_cs='null',
                d_rpt='129',
                spam_report='0',
                deletable='0',
                address='+15555550001~+15555550003~+15555550005~+15555550004',
                date='1429235500000',
                sim_slot='0',
                sim_imsi='null',
                hidden='0',
                resp_txt='null',
                ct_cls='null',
                tr_id='D90417015140600035000060000',
                locked='0',
                m_type='132',
                sub_id='-1',
                retr_st='null',
                safe_message='0',
                d_tm='null',
                st='null',
                m_cls='personal',
                exp='null',
                v='16',
                date_sent='0',
                read_status='null',
                parts=(
                    MMSPart(
                        name='123_1.smil',
                        seq='-1',
                        cl='0.smil',
                        text='<smil>\n<head>\n<layout>\n <root-layout/>\n<region id="Text" top="70%" left="0%" height="30%" width="100%" fit="scroll"/>\n<region id="Image" top="0%" left="0%" height="70%" width="100%" fit="meet"/>\n</layout>\n</head>\n<body>\n<par dur="10s">\n<text src="text_0.txt" region="Text"/>\n</par>\n</body>\n</smil>\n',
                        cid='<0.smil>',
                        chset='null',
                        cd='null',
                        ctt_t='null',
                        ctt_s='null',
                        data=None,
                        fn='null',
                        ct='application/smil'),
                    MMSPart(
                        name='text_0.txt',
                        seq='0',
                        cl='text_0.txt',
                        text='And only let in two.',
                        cid='<0>',
                        chset='106',
                        cd='attachment',
                        ctt_t='null',
                        ctt_s='null',
                        data=None,
                        fn='null',
                        ct='text/plain')),
                addresses=(
                    MMSAddress(
                        charset='106',
                        type='137',
                        address='+15555550005'),
                    MMSAddress(
                        charset='106',
                        type='151',
                        address='+15555550004'),
                    MMSAddress(
                        charset='106',
                        type='151',
                        address='+15555550003'),
                    MMSAddress(
                        charset='106',
                        type='151',
                        address='+15555550002'),
                    MMSAddress(
                        charset='106',
                        type='151',
                        address='+15555550001')))]
        expected_string = '' + \
            '<smses count="1">' + \
            '<mms address="+15555550001~+15555550003~+15555550005~+15555550004" app_id="0" callback_set="0" contact_name="Ted Turner, Nancy Edgar, Antonio Scott, Max Hall" creator="null" ct_cls="null" ct_l="null" ct_t="application/vnd.wap.multipart.related" d_rpt="129" d_tm="null" date="1429235500000" date_sent="0" deletable="0" exp="null" hidden="0" locked="0" m_cls="personal" m_id="479E1FAE-E4A4-71F4-7B68-A8D385BCA5DE" m_size="318" m_type="132" msg_box="1" msg_id="0" pri="129" read="1" read_status="null" readable_date="Apr 16, 2015 9:51:40 PM" reserved="0" resp_st="null" resp_txt="null" retr_st="null" retr_txt="null" retr_txt_cs="null" rpt_a="null" rr="null" safe_message="0" seen="0" sim_imsi="null" sim_slot="0" spam_report="0" st="null" sub="null" sub_cs="null" sub_id="-1" text_only="1" tr_id="D90417015140600035000060000" v="16">' + \
            '<parts>' + \
            '<part cd="null" chset="null" cid="&lt;0.smil&gt;" cl="0.smil" ct="application/smil" ctt_s="null" ctt_t="null" fn="null" name="123_1.smil" seq="-1" text="&lt;smil&gt;&#10;&lt;head&gt;&#10;&lt;layout&gt;&#10; &lt;root-layout/&gt;&#10;&lt;region id=&quot;Text&quot; top=&quot;70%&quot; left=&quot;0%&quot; height=&quot;30%&quot; width=&quot;100%&quot; fit=&quot;scroll&quot;/&gt;&#10;&lt;region id=&quot;Image&quot; top=&quot;0%&quot; left=&quot;0%&quot; height=&quot;70%&quot; width=&quot;100%&quot; fit=&quot;meet&quot;/&gt;&#10;&lt;/layout&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;par dur=&quot;10s&quot;&gt;&#10;&lt;text src=&quot;text_0.txt&quot; region=&quot;Text&quot;/&gt;&#10;&lt;/par&gt;&#10;&lt;/body&gt;&#10;&lt;/smil&gt;&#10;" />' + \
            '<part cd="attachment" chset="106" cid="&lt;0&gt;" cl="text_0.txt" ct="text/plain" ctt_s="null" ctt_t="null" fn="null" name="text_0.txt" seq="0" text="And only let in two." />' + \
            '</parts>' + \
            '<addresses>' + \
            '<address address="+15555550005" charset="106" type="137" />' + \
            '<address address="+15555550004" charset="106" type="151" />' + \
            '<address address="+15555550003" charset="106" type="151" />' + \
            '<address address="+15555550002" charset="106" type="151" />' + \
            '<address address="+15555550001" charset="106" type="151" />' + \
            '</addresses>' + \
            '</mms>' + \
            '</smses>'

        tree = self.backup_control.build_tree(smses)

        self.assert_tree_as_string(tree, expected_string)

if __name__ == '__main__':
    unittest.main()
