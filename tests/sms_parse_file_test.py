'''
phone_communication_backup_coalescer: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Phillip Green II
Licensed under MIT
'''

import unittest
import os.path
import tempfile
import shutil
import datetime

import phone_communication_backup_coalescer.sms as sms
from phone_communication_backup_coalescer.utils import ParseSupport


class SmsParseFileTestCase(unittest.TestCase):
    def setUp(self):
        self.backup_control = sms.SmsBackupControl(ParseSupport())
        self.temp_dir = tempfile.mkdtemp('sms-parse-file-test')

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_filename_pattern(self):
        self.assertIsNotNone(self.backup_control.filename_pattern)

    def test_parse_file(self):
        full_file_name = os.path.join('tests', 'data', 'sms-test.xml')
        smses = self.backup_control.parse_file(full_file_name)

        self.assertEqual(len(smses), 15)
        self.assertEqual(smses[0], sms.SMS(
            body='Free AT&T msg: Your Authorized user was changed for acct # ending in XXXX. If this was done in error, call 800-331-0500 or 611 from your wireless phone.',
            service_center='+13123149623',
            protocol='0',
            read='1',
            sc_toa='null',
            readable_date='Jul 15, 2013 7:07:22 PM',
            date_sent='1373929642000',
            status='-1',
            address='7535',
            date='1373929642000',
            locked='0',
            contact_name='(Unknown)',
            toa='null',
            type='1',
            subject='null'))
        self.assertEqual(smses[1], sms.SMS(
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
            subject='null'))
        self.assertEqual(smses[2], sms.SMS(
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
            subject='null'))
        self.assertEqual(smses[3], sms.SMS(
            body='G',
            service_center='+13123149619',
            protocol='0',
            read='1',
            sc_toa='null',
            readable_date='Jul 15, 2013 10:42:54 PM',
            date_sent='1373942574000',
            status='-1',
            address='+15555550000',
            date='1373942574000',
            locked='0',
            contact_name='Jane Smith',
            toa='null',
            type='1',
            subject='null'))
        self.assertEqual(smses[4], sms.SMS(
            body="I'm home",
            service_center='+13123149619',
            protocol='0',
            read='1',
            sc_toa='null',
            readable_date='Jul 15, 2013 11:34:08 PM',
            date_sent='1373945648000',
            status='-1',
            address='+15555550000',
            date='1373945648000',
            locked='0',
            contact_name='Jane Smith',
            toa='null',
            type='1',
            subject='null'))
        self.assertEqual(smses[5], sms.SMS(
            body='AT&T msg: Your online registration code is: XXXXXXXX. ',
            service_center='+13123149619',
            protocol='0',
            read='1',
            sc_toa='null',
            readable_date='Jul 15, 2013 11:48:19 PM',
            date_sent='1373946499000', status='-1',
            address='7535',
            date='1373946499000',
            locked='0',
            contact_name='(Unknown)',
            toa='null',
            type='1',
            subject='null'))
        self.assertEqual(smses[6], sms.MMS(
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
                sms.MMSPart(
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
                sms.MMSPart(
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
            addresses=()))
        self.assertEqual(smses[7], sms.MMS(
            callback_set='0',
            m_id='69BF9BA8-608D-71E4-AE83-D8D385BFFBCE',
            reserved='0',
            creator=None,
            msg_id='0',
            pri='129',
            app_id='0',
            retr_txt='null',
            sub_cs='null',
            seen='0',
            contact_name='Ted Turner',
            sub='null',
            rr='null',
            text_only='1',
            ct_t='application/vnd.wap.multipart.related',
            ct_l='null',
            m_size='null',
            resp_st='null',
            msg_box='1',
            readable_date='Oct 30, 2014 7:35:24 PM',
            rpt_a='null',
            read='1',
            retr_txt_cs='null',
            d_rpt='129',
            spam_report=None,
            deletable='0',
            address='+15555550001',
            date='1414712124000',
            sim_slot=None,
            sim_imsi=None,
            hidden='0',
            resp_txt='null',
            ct_cls='null',
            tr_id='DG1030233524600048000010000',
            locked='0',
            m_type='132',
            sub_id=None,
            retr_st='null',
            safe_message=None,
            d_tm='null',
            st='null',
            m_cls='personal',
            exp='null',
            v='16',
            date_sent='0',
            read_status='null',
            parts=(
                sms.MMSPart(
                    name='smil.xml',
                    seq='-1',
                    cl='smil.xml',
                    text='<smil><head><layout><root-layout width="320px" height="480px"/><region id="Image" left="0" top="0" width="320px" height="320px" fit="meet"/><region id="Text" left="0" top="320" width="320px" height="160px" fit="meet"/></layout></head><body><par dur="5000ms"><text src="text_0.txt" region="Text"/></par></body></smil>',
                    cid='<smil>',
                    chset='null',
                    cd='null',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='application/smil'),
                sms.MMSPart(
                    name='text_0.txt',
                    seq='0',
                    cl='text_0.txt',
                    text="Maybe.  I'm still at work.",
                    cid='<text_0>',
                    chset='106',
                    cd='null',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='text/plain')),
            addresses=()))
        self.assertEqual(smses[8], sms.MMS(
            callback_set='0',
            m_id='103122142050001500002',
            reserved='0',
            creator=None,
            msg_id='0',
            pri='129',
            app_id='0',
            retr_txt='null',
            sub_cs='null',
            seen='1',
            contact_name='(Unknown)',
            sub='',
            rr='129',
            text_only='1',
            ct_t='application/vnd.wap.multipart.related',
            ct_l='null',
            m_size='16',
            resp_st='128',
            msg_box='2',
            readable_date='Oct 31, 2014 6:14:13 PM',
            rpt_a='null',
            read='1',
            retr_txt_cs='null',
            d_rpt='129',
            spam_report=None,
            deletable='0',
            address='lamer000@aol.com',
            date='1414793653000',
            sim_slot=None,
            sim_imsi=None,
            hidden='0',
            resp_txt='null',
            ct_cls='null',
            tr_id='T1496845e177',
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
                sms.MMSPart(
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
                sms.MMSPart(
                    name='null',
                    seq='0',
                    cl='text_0.txt',
                    text='Happy Birthday! ',
                    cid='<text_0.txt>',
                    chset='106',
                    cd='null',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='text/plain')),
            addresses=()))
        self.assertEqual(smses[9], sms.MMS(
            callback_set='0',
            m_id='F743329A-620A-71E4-BC32-D8D385BCF5CE',
            reserved='0',
            creator=None,
            msg_id='0',
            pri='129',
            app_id='0',
            retr_txt='null',
            sub_cs='null',
            seen='1',
            contact_name='Ted Turner',
            sub='null',
            rr='null',
            text_only='0',
            ct_t='application/vnd.wap.multipart.related',
            ct_l='null',
            m_size='null',
            resp_st='null',
            msg_box='1',
            readable_date='Nov 1, 2014 5:06:43 PM',
            rpt_a='null',
            read='1',
            retr_txt_cs='null',
            d_rpt='129',
            spam_report=None,
            deletable='0',
            address='+15555550001',
            date='1414876003000',
            sim_slot=None,
            sim_imsi=None,
            hidden='0',
            resp_txt='null',
            ct_cls='null',
            tr_id='E81101210643700022000000000',
            locked='0',
            m_type='132',
            sub_id=None,
            retr_st='null',
            safe_message=None,
            d_tm='null',
            st='null',
            m_cls='personal',
            exp='null',
            v='16',
            date_sent='0',
            read_status='null',
            parts=(
                sms.MMSPart(
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
                sms.MMSPart(
                    name='text_0.txt',
                    seq='0',
                    cl='text_0.txt',
                    text='Mountaineers are making me crazy today. You guys watching? ',
                    cid='<0>',
                    chset='106',
                    cd='attachment',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='text/plain')),
            addresses=()))
        self.assertEqual(smses[10], sms.MMS(
            callback_set='0',
            m_id='11012127235060700005',
            reserved='0',
            creator=None,
            msg_id='0',
            pri='null',
            app_id='0',
            retr_txt='null',
            sub_cs='null',
            seen='1',
            contact_name='Ted Turner',
            sub='null',
            rr='null',
            text_only='0',
            ct_t='application/vnd.wap.multipart.related',
            ct_l='null',
            m_size='null',
            resp_st='null',
            msg_box='1',
            readable_date='Nov 1, 2014 5:07:28 PM',
            rpt_a='null',
            read='1',
            retr_txt_cs='null',
            d_rpt='129',
            spam_report=None,
            deletable='0',
            address='+15555550001',
            date='1414876048000',
            sim_slot=None,
            sim_imsi=None,
            hidden='0',
            resp_txt='null',
            ct_cls='null',
            tr_id='A35101210728200007000050501',
            locked='0',
            m_type='132',
            sub_id=None,
            retr_st='null',
            safe_message=None,
            d_tm='null',
            st='null',
            m_cls='null',
            exp='null',
            v='16',
            date_sent='0',
            read_status='null',
            parts=(
                sms.MMSPart(
                    name='null',
                    seq='-1',
                    cl='null',
                    text='<smil>\n<head>\n<layout>\n <root-layout/>\n<region id="Text" top="70%" left="0%" height="30%" width="100%" fit="scroll"/>\n<region id="Image" top="0%" left="0%" height="70%" width="100%" fit="meet"/>\n</layout>\n</head>\n<body>\n<par dur="10s">\n<text src="text_0.txt" region="Text"/>\n</par>\n</body>\n</smil>\n',
                    cid='<0.smil>',
                    chset='null',
                    cd='null',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='application/smil'),
                sms.MMSPart(
                    name='null',
                    seq='0',
                    cl='text_0.txt',
                    text='Listening ',
                    cid='<0>',
                    chset='3',
                    cd='attachment',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='text/plain')),
            addresses=()))
        self.assertEqual(smses[11], sms.MMS(
            callback_set='0',
            m_id='110121413160005306005',
            reserved='0',
            creator=None,
            msg_id='0',
            pri='null',
            app_id='0',
            retr_txt='null',
            sub_cs='null',
            seen='1',
            contact_name='Ted Turner',
            sub='null',
            rr='null',
            text_only='0',
            ct_t='application/vnd.wap.multipart.related',
            ct_l='null',
            m_size='null',
            resp_st='null',
            msg_box='1',
            readable_date='Nov 1, 2014 5:41:31 PM',
            rpt_a='null',
            read='1',
            retr_txt_cs='null',
            d_rpt='129',
            spam_report=None,
            deletable='0',
            address='+15555550001',
            date='1414878091000',
            sim_slot=None,
            sim_imsi=None,
            hidden='0',
            resp_txt='null',
            ct_cls='null',
            tr_id='D51101214731200053000050001',
            locked='0',
            m_type='132',
            sub_id=None,
            retr_st='null',
            safe_message=None,
            d_tm='null',
            st='null',
            m_cls='null',
            exp='null',
            v='16',
            date_sent='0',
            read_status='null',
            parts=(
                sms.MMSPart(
                    name='null',
                    seq='-1',
                    cl='null',
                    text='<smil>\n<head>\n<layout>\n <root-layout/>\n<region id="Text" top="70%" left="0%" height="30%" width="100%" fit="scroll"/>\n<region id="Image" top="0%" left="0%" height="70%" width="100%" fit="meet"/>\n</layout>\n</head>\n<body>\n<par dur="10s">\n<text src="text_0.txt" region="Text"/>\n</par>\n</body>\n</smil>\n',
                    cid='<0.smil>',
                    chset='null',
                    cd='null',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='application/smil'),
                sms.MMSPart(
                    name='null',
                    seq='0',
                    cl='text_0.txt',
                    text='Remember that warren sapp touchdown dance?',
                    cid='<0>',
                    chset='3',
                    cd='attachment',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='text/plain')),
            addresses=()))
        self.assertEqual(smses[12], sms.MMS(
            callback_set='0',
            m_id='110121555670002700005',
            reserved='0',
            creator=None,
            msg_id='0',
            pri='null',
            app_id='0',
            retr_txt='null',
            sub_cs='null',
            seen='1',
            contact_name='Ted Turner',
            sub='null',
            rr='null',
            text_only='0',
            ct_t='application/vnd.wap.multipart.related',
            ct_l='null',
            m_size='null',
            resp_st='null',
            msg_box='1',
            readable_date='Nov 1, 2014 5:55:56 PM',
            rpt_a='null',
            read='1',
            retr_txt_cs='null',
            d_rpt='129',
            spam_report=None,
            deletable='0',
            address='+15555550001',
            date='1414878956000',
            sim_slot=None,
            sim_imsi=None,
            hidden='0',
            resp_txt='null',
            ct_cls='null',
            tr_id='E91201315556401027000050001',
            locked='0',
            m_type='132',
            sub_id=None,
            retr_st='null',
            safe_message=None,
            d_tm='null',
            st='null',
            m_cls='null',
            exp='null',
            v='16',
            date_sent='0',
            read_status='null',
            parts=(
                sms.MMSPart(
                    name='null',
                    seq='-1',
                    cl='null',
                    text='<smil>\n<head>\n<layout>\n <root-layout/>\n<region id="Text" top="70%" left="0%" height="30%" width="100%" fit="scroll"/>\n<region id="Image" top="0%" left="0%" height="70%" width="100%" fit="meet"/>\n</layout>\n</head>\n<body>\n<par dur="10s">\n<text src="text_0.txt" region="Text"/>\n</par>\n</body>\n</smil>\n',
                    cid='<0.smil>',
                    chset='null',
                    cd='null',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='application/smil'),
                sms.MMSPart(
                    name='null',
                    seq='0',
                    cl='text_0.txt',
                    text='Brad paisley',
                    cid='<0>',
                    chset='3',
                    cd='attachment',
                    ctt_t='null',
                    ctt_s='null',
                    data=None,
                    fn='null',
                    ct='text/plain')),
            addresses=()))
        # smses[13] through smses[14] handled in separate tests

    def test_parse_file_with_image(self):
        full_file_name = os.path.join('tests', 'data', 'sms-test.xml')
        smses = self.backup_control.parse_file(full_file_name)

        self.assertEqual(smses[13], sms.MMS(
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
                sms.MMSPart(
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
                sms.MMSPart(
                    name='null',
                    seq='0',
                    cl='duck.png',
                    text='null',
                    cid='<duck>',
                    chset='null',
                    cd='null',
                    ctt_t='null',
                    ctt_s='null',
                    data='iVBORw0KGgoAAAANSUhEUgAAALkAAAB6CAYAAADj0fJGAAAACXBIWXMAAAsTAAALEwEAmpwYAAAABmJLR0QA/wD/AP+gvaeTAAAY3ElEQVR42u2dCXhU1dmAB8G69EetVWxta62laNtHaq11qf2fWnlotS1arFZbbVW0UBAqKFhw+6MY2ZRFQxJCQtiXsIVFAoQEyJ5MklmTuTOTmcxkJrPv+5LJ958zuQkh62zAvZNznud9FDIZ7tzzzrnf+c537uVwWNgAONcifol4AbEIsRqxBbEbcQhxAnEMsR+xA5GN+BAxG/FHxB2IcRzSSGOQ0A8i5iEKEHxEGAFJYkKcRGQiniHik3YlxMbiHUD4UyB0rMgRHyHuIb1A2qUQewLid4hChPMyij0cPMQSxPdI75CWrNzjEf9EtDNA7KHopmP9yaS3SItX7nGIpxBihso9kDA9gf026T3SYhH8YUQNS+QeiA/xKeJ60pOkDTd6v43oYqng/RGSEIa0gYLfQGdLII1w4JCL9C5pWPCfIqg0E7w/ONc+nvT02BX8Zwh76oRCFwS4B3ET00TfiriK9PjYE3wywpicPLciFiFqEVa4uFkQhxA/ZoroX5JV07El+HX05CxBYW5H7EOEYfSG5rEwmymiv0p6f+xInpuoKN3dz0F9/RlYsmQJzJgxA6ZNmwYvv/wy7N69GwKBwDCiexFfZ0qK8SfEgPQX/MFEJTGbX4Cnn34a8NsMxX333QdyuXwY0e9hymh+hoQt6Z8Lr05Ejq6ue+GBB+4fVvBepk+fPoTgbsS1TJqI/onYkL6SP5SoGDt3zh9V8F6CweAAyecyLdtSTmxIX8kLEhUjMzM2yW+88cYBgu9GjGNi/nwKMSI9Q5WEU4bnzy+LSfKsrCxabpx5eQ8xgamLRAuJFekn+ZTkpLgd3nnntWHlnjBhAqxYsQIiESx3CeJ+pq+EHiRWpJ/kTyUvxtVw7tzTMHfuM3DvvT9G3AuPPvoryMhYCBS1Df18GeI7bFnubyVWpJ/ks1IvykQmhyOjYSRWpJ/kb6RxEVYiuIgV6Sa5kTOXiH0RKmJFOgk+izMRvozudidyX6COmJEugs/mXA9zOGXwH9Sx3UTufqwndqTLCD6HU4FEhygqInc//kIMYbvgr3BuQmLX9QmO2UfkprHhcmNiCbtDlFsQzRcJjlmECBHJSajCdsH/xZmChJYPEryXr8a84G7Et4gpjEhrT0hE8N8gka3DCo5ZgLCPacnVRC9GCI5rqTbGK/g/kMTBEQXvZe2YzrRQRDFGSL4CoYvtxQs418AczsaY5O7P0TEruYwodsUFf53uC8PoL57D+RESlhe34Jg5iKoxKXkH0eyKCv4v+kat0fvQj5ZB+TvCnZDgvfwbUTvmJDcR1a6Y4P/uJ/jwI3l0BXM2pyApuQeO6HsQkTEjeRBxNVHusgs+b4DgGOVQk8ufIjHFKRO8PyvHVNZlKtHusgo+f5h+EA+Mv19DMnqHkbQLYUAoECJ6pbMccRxRhNiKyEZkjch76ArhRb+b/pIvJupdNsHfHKEf6nvDk18jjiDMiHOIXMRCNKo/icT/GbzOuQ0yUnefPzp/OQMhSmPJ5QktRJAWj0dX0TdbHfmuCUjg7yKRp2GRr8BB4kep/IPBj1JJlh39bwJKf95b8YO3EI8iptOPXHyGflzjP+nU1zx6AoV3Wr2E+CviacSTiGmIBxA/oG+HPW6MCv5NxKkY+uA4Uw74Grpjm9JQdHzbOAN9Z9/uS/D+IYSefizNOcR2xMf0F+RxxF3pNglGn+d+vCElxvOzj4kf4G5EBkJKirxSRgRnGRDF9BfgWfrOCuNZJvcE+kkl8Tz2spDJHwjH7b+gl2Zb0+QRLEy8ytQj1tEh020M9uFXCEECnzGLLd/ga+nRPUDEvORI6bugvcyESko69s5PItRbzbZY7IcIBRHx8pYoIPLoOxWPu4x9PYnOnNiSPP7/Y+Ok4z9EvCu6kouTA0vpyd+NlyDb9gRiVwofN/8GGyV/hcjGuCfgNSL2I1Yh5tDxPU51/pKe4H4bhz4D+C79c5waXYZTfQjrJTi+Z9hagEPkIsTKI2yUvIB0HCEO7mSj5BLScYQ4uIZtgv+EdBohntuCsHEUzyQdR4gDPtsE/xpCSzqOEAd72Sb5HNJphLRdCKILc5Sk0whx8jybJH+ZdBghbbcg0rs/ZKTDCAmUF19LYnFCOtPGFsEn0VVwpNMI8VLIBsFvQQhJZxES5CU25MTrSEcRkuB2pkv+OekkQtreVZi+H8vY6hR8+7wu+gkdQYQf4UN46f8G6L8P068jDx8bjWwmC/4NhIWVJ7abFtGNsCIMCA2iHSFHSBAihBDBR/AQTYjGJGii34dPv6+Y/nfk9APKtPRxWOnjGjuPuZnJZMlXsOIk4pHVRkskpwVLVtjLRRP9ZWtDdNL3pgymleBWxpbX0lukfIw9eQ56dBSyROZ4weKrES7WS57F5FF8HSNPmosOAxrHEBJ6PsA+wfFtK37K5KV7HSNPXMsYE7wXGSslP8TkUfwhxp44D6J1jAkupbM67BIc32HtZ2TCmWzY0pHGoUsrPZH2sDYW/5zpufESVp3QUL+JaAudwmNLdoVPC91OpxdddP6d3ZNNvNfgeqZLLmDFyfTRaTc2hi9i+th9nHTMi09nQzGWifFyS9NsUulPG8G3saWkNsTolUxBmubF2S+4EXEzWyRn9i58ZRpKrkoLyf/Gpj2cXMafULz8TaVJetBx5c+n0zkRFKqfA1f4NxAql4Cg/WMQdqwDcecXIFBlAl+xDLjiV4FSPApm8y1DvcdXbLvdRDGrMivmfpkVJmdVmuhJMj5WCzOyKF1d40HW/jiIOz4CuXUTdIY2j4jSsQkk+s9AQD0LHt8Nve+D53DfYZvkb7O6TNZNZy7ktFTCFFUZxiKxgL7CtNPHgL+ATnqyzLAnYBstd0Gt6L2Y5B6I2p0HXNlqUGkfwRuUp3HY1tBBT2ad3E46VhcxZNTGXywFXR3JwPPVpv41iDRr45Z7IE2acu676wyzMjLgKjaKzp4H17oZHnczTHSF+hFo1WclLXhHsFgt9sPmRnNk88dZpllslPwtVo3kNjo84TNEbB49qTQza+eQyToF+Kp1SQuuDe1wtfo927HkmLK2wObV22x/YrzYb2bo7sg74nxhf433gzOUcz1lXO+WaJeBXPMcWB13DDphodAE0Om/AyJqOvClrwNP9hbwlR+CqCMTeG3LoIl6ExpFfwd5+/1gtd50eTdRWOmdQEpaNjEtXqpFFtMxuIL+9yzMXdgJh6+GevG7SQveGSrokgY6DvcK3svBWu/Gf7+nYeYE9LnnisbnH3c8V9XRlS1yR/oOWhHgVka/tYE8NKvOBkXnX9FsfEL0hOmMU6CZmo8uextBhSYhI50UuW0TtGhXgZCaCT7f/1z5iWmg355NN10v4qDTklZaVCv9Zwf9czddLNW7xzPCvkl5i/z30O7alKTg+d1tAVHpQMF7WVVgXsjhZDArPn/ssbMTdpS55/PskUEH3OLvKtCE9lj7YjBfHvAVi6FRMgdEnRsTm5FLV0K79ldkc+9lxuW6HgTKD5IexRWBxorhBMeUSgKbHn9S/kNGSZ533PmCwBEZ9qCpgH4/ujyFozlSzx7gG7hQpyhN6kS1GnKgUfwidHePJwJeJlSae0Bqzk2q35TBSu5IgmPwYPn2p/pnGSP4e5/pvl+l7sod7cDbAryzCvceEFj4IA9QILS0gMS8J6kTpkFXhXrBLNQB44iElwG+ZCZ0BhPvL1XwVOtonvSSe9SxmDGS7yjzvBrLQQtckW2NBqUFC94Lt+McdPiTu/ThRQhK9Wci4WWAK3o10Rg8ogqekMYqOGbnWfdyxkj+lSiwOpaDrtKGq4Sebkoa6HT2St6o44HSVZB0jMdXZ4HJ+kMi4iUGJwkSEVweaDkdj+CYww2+9YyR/JwqNOoB1xm7DjbZuiUtfqDE/m4pFdC6sOQCcwtQ1p0pSEdtBm7rW9F0JJHx0sGTLkggiyI8E6/gmOJG3wbGSN5g6hrxYIUeKKjWhmuw4L1g0fGI3uJsBZF+X0okx2FLu3oqkfFShiviV+PKgycqOGZ3mfsTxkiOJp0jHmyDuWsn1xIR95e8l2az0SSx7E6J5JgGwUtExhShtzwAcuNSkFlyo3lxbQBdLdWngG8SQ7OuFsSm/SOsZG73DLXQEw/5xxzvMEbyM5JQ1kgHW60LHxe4uqmhJK/WhCTNZuqMNlQYTIXkYvUHRNCky2YnANXxCiidgxd8pPYD0OqWROdTIlsrkr4UtMH8i2tRQkUGid+5MxnBeY7I5sWZnS8wRvJ9FZ5FIx1wpSZ8Bk84h5K8TBZsaHZAAeU37cMnJ1nJRR3riaj98HiuA4PlHlDppoGk/S/QqnwG2junRWtPvN7rBr2+u/sqkKheHzZN2O7ZCiJrU192TOaVQG3fekd+d3uwTIAX/5IRPFrDIg3l/WGmZApjJP98p/XhkeLy8+pQxVCC823dVHlb8PiFldFIvjJYV9O7aJTQApE+h8iN8PomIqGfhRbtpyAx5UQ3KWj9eVGiGxbQ34k1meg1f7moREJremzUJXux+RRIfZI+0cVoROfrTzqTDU/6s2GPdTGHc3YCYyTHNcD7Kj3/HTZ1qAkPKXmZPNTId8Ggbz3lN+/tCB7sTERyiZH9kpvNN4NM8Qg0t74EzdIFwG9bGt1xg//Lk86HppYXQaZ8ECyWm4f8/U7jA+iKtjoaQ49aBRjIA6F6JejMP0dfjK+D3Lxy9NJY/xYUlzfSkku70VXYXKkO8upMXYWpEPwQ15uzKEN9F+OKs5Z9ob/1GM83ZL68Uh0qFw0IV84pgqJ6Y9eukT4szq1qQrvso9ZBuAqhUV0CDZo6qFHyQYFGKsqUDRLdhyDXPgse782skNvumARc4T+gtXNt9DOM9Jnb7JugpfMzaBK/CA7XN/veQ65+AuTW7LgHB6k5GxrEb8RceNXmPgh8q8rZ4g8qcH82miNUeXvwYLKC43T0up3WZzlMbRkbTd86wvX+n8h1cQ1LVWe4ROjukRzLflYZbK4xhHbH8qFxfIeLebShbd4hY3DjgeiCktxP0ZMh3qDXUMbPQWd5hLFyRyJXAdX+FPCUa+NeMsfhR7PiM5Cp/gAduodBZs1JfJ2h4zTwNQdi2ORwUItDk1p9uKTZ2bP2IXB2U6elgbJkBMeVq8s3md7ANRqMriWfPRuuzi6y/fE43/8R/lbWG7o2o7h771lFUHJOGeShE3G6yR7ZEu8JQCNGoTJYW4uL7HtPttBQDAKzGPqXCQhMlUOP9mhk7DA8zjjBA8GJaARdkND+yP4IOrbAGf4p0AQKEy94s1dDrYoHbY6tw8h9SCMLyL66KHPWGT7daI20YtFLWvxVCY/gytDm9zd0LsjIYFAcHl+ruW5TsWNpKuI1PLLjBYZW6zELzyi8SHDKIwH098NfYm0bweq4e9CGDY9nIhgsU0Gl+y0oNL8HrfEhsDluB7//mksquA/FwHWi/6ZkfaCCKo2eA56xDsXMiYkucdaCzEdBtez0oJoTKqA7MOw6iKnrYLU2JCwR+asTSRXuqXBnL8/V/4HD9rZoue53DaZISmbeAg/kl8qCta1+n6qnDkYW6QlVmqHdu23EjqQ6l0A43LP0b7HfCVLtbJAY1kdHUlynjqsaFXT2Qap/F9T6/42m1UaS1WKZBJRyOrSo5qIJ4ofQqvscvecGEGuWQ2vHQhDLngK98QcDfm8ccFEMjP+9ZAWXWbdAg7anshNnPYa7mo06ktsqeormNPzotrT24PmmWPPdfGdXYfYBe1ZxvWdtra5r1NfjbFwpFcr+KMc4581M422cdGh419CGXfYPUiH5eWVoLxdNdC5MZCMyodOqa7FVmEetZUYTK4PlJ9CmfSo62Rrt9XgiJmpfAm7v4BvhBEPXgaT9zyA1rQO1N2/EuFluywYeNQtcnlt7drl3TEu6LruvOK3zQLQGqPeKhkslKPuxuN+HcpwOU95Oe4PeqY63T7C0Gw/af/uLXzTeMv997eMf5xrnFVW7Pylu8G04KQ5sPkMFNh9p8mXtr/asXLvdumjxJ4YZv56huIOTbu399ea7D9a6s5NeKJAFTvEdF7I1eKGpShNqwD+T+G27lcGauo7gAR1enBi0q8iTBxX8kaUcepEpE4k+6cLobfse8No+GHXL3sXpOiSkag1I5L8BvnJlykoZ6pQlKNSQXBS6Ca08UHm3xrCRuDCgDh6X4xCw2R4sEri7JU3WCBVvn6BwZePMmW2TOKRxOEvX6B87IwtsSkZyNMG5KO9eows3C1ywdeDr8C7wtgC/HHci7sye+3scB57+fIIlA+9CKPw1sDm/DzzlqoSlrJQcB67ycMok743H+4PDFrG5ZOiNJqFddrwyKQsojg1cnWwwdlX1FNDFlxXJP+56mdjdr737mf7JE4JAwiN6mSJUHR3B3WgE7ww3812wI5YJK1ffUVKn1RnE9habNrTVH/feUnQVaG1/DgTKjxIWUu3bAiJLPYqhBSA2pqb6skpeNkjy6Ghuru2TWhU8KcE7syR+654RY2tXZEejNSKMpz+ONvpW/nel4kZi9qDbVmim5h11rKmPYZIyeCQPVDRaIlS1Nlw91Ag+7O+J/Gfxl6PeGK7p2XdqLMI5eCyAJlRkjKWcoEpWgmLpLQkL2ebcFY2ZsYQV0gYUNuUnLXlN20mQ0EVTsoA8LA10eCR+g5Vvt2v639MkVlCfFJVKAmtjee0JUWBN/lf27xOjh2mLFxu+/kmu6fkjjb71o9WkX8jLoglOsXNntSYcd53EGWmQj+P3BktX2dCjfSQfF4rhWyXgzII6eFSpCe0194Y6cmcRNOrEIDTsT1hIynawT8hWFEfXKY4leFOe7Z6O4H49Tu9VqUQtXLOzA12t5P3DuCZH/LF1dPFO3bV51Wbrd/dWeZbgjNjAxT28YR33165yz6I1OW4Sh8fSHpomuu3N5YY/rdluXVjc5FuLZ+Nl8gA62aHorPwrvj93R7n742VrDK+9tkj54L/eUkxJ5AqAJqcULvltsnYfiPd3W/3ebfUGG09od2grFZQUx7RYMHWwWIVlwyGBNrTNh/PKI8nZYjkGlPfCJLFWVQ9ye+/2v4KwNrTDrQntseDaHXXwmAJv/G0PnmvG966RB6Qn8JdwYBx9XhXaWakKSgYVwKHPmojkJ1v8OT09A1dl5pnu23LS9WpRlWcpmgtl4BqlrSec//zgS8O96OfjiL2XrBWNRyf77fjTXBGKa4404p1KiXQ+1xIRYnmO8f0Vo8X/eIUWhwo4z4wzPlhOfFuOOp21UuQNKFr8oTY88tbqgrJTEu8BfBVJdI7S7IgUnBD5awdKLnAnJnnBcecC4hgD2op80+SK9vgmryiGlzTb4x/F+1bnnD1py9EkH4kaffgov98GEj56zyNN/pNJFza1h/YNHM15jvglP9USyF26Qn8nMYwhLeew+7FqTVdM6Ui8CocmnknJhOXENfCnqVDC+xbr9F37ef1y/Lhg7VC9pzwVi2QnhIEzOMfdF5Pb4ovJcZ3Rl/vsfyZmMax9sdf6cCkVWDdS55W3hb7IOWx/rJjrzUxGIpyyrDdGqLOKcMKbAxptkW31prCg/4hbzPWfT4XkIi/kH+P5K/EXMZpFMoR58axYbthrm83K+4OPhTZ3qfobucWO5480epcjofPwpLRcGco72uTNzDtme3HBMv2t+HW5h20vJTuSV3WERTW6rq3JvE9lR6iybyRHX5wDdakZyXtFPyH2n0GTdklFRzimL0+pNLRp3S77M0TwNGjz5rV/67QkkJWoQFw0ip9qDZ1OVkQUshxsdvTUYeOY/GiztyRVkvfd/rjOtyfnsGsVvt83DkP6pwHx/0cHAjQgbD3tevv9DaYfETvSqOFa91hz8gPZX+Wp4LsiBamQsPduYngyXEoF96ZScPzEhhX51lmkt8dsg3E5h1yzms3xlf0erves+rTQujBVIqIvy/ZafUR4qjXQWGtMzd7IXvBK8qoC80TS12O44dgz66BrZnkMhWJ41N9+yrXs7QzdLbMWqe8qpUI5qZLxrDK8f8sJ96FUCo7i+/WLVpgmk14mLdqWrtPfue2Uc16J2JeFV1ex0HinCi4dKJOH8g43eD9Yu938m/4TsnV7rHFfBYZj02F7RsYXlgcP1PjWp+L9dp3zrM1Yb5tKepa0pNrsDN31hSXOjGSFPNro29C76PLKUv2d6/dYl1fEcOPUIa8IaHK5Zps144V5bd8jPURaasKdHPek7aWeFYkKfqTJm5W5yXz/gBBqwie55hl7znvWxDoxxq/bWe5ZtSLf9AQASf+RluL2t9m6W74ssi2t0sSeqcFhzo4y18p3VnXePdz73nkf76ZFGZonVhZYFhzm+j6PFquhkbpa0xUtWsN/Ptzg+WxFvmX+ggzd7yZPlt9AeoO0S5enARiXmW+ZdrTZt3Kkzbt4xC2TBr5Yvc30PA53yJkjjXXt5pvlN7z5seGh1YXWWYUlriVFVe6PDnG9n2wvdS3NKrLMXbrC8PjUqQJSd53i9v9tRRwCGsiViQAAAABJRU5ErkJggg==',
                    fn='duck.png',
                    ct='image/png')),
            addresses=()))

    def test_parse_file_with_multiple_addresses(self):
        full_file_name = os.path.join('tests', 'data', 'sms-test.xml')
        smses = self.backup_control.parse_file(full_file_name)

        self.assertEqual(smses[14], sms.MMS(
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
                sms.MMSPart(
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
                sms.MMSPart(
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
                sms.MMSAddress(
                    charset='106',
                    type='137',
                    address='+15555550005'),
                sms.MMSAddress(
                    charset='106',
                    type='151',
                    address='+15555550004'),
                sms.MMSAddress(
                    charset='106',
                    type='151',
                    address='+15555550003'),
                sms.MMSAddress(
                    charset='106',
                    type='151',
                    address='+15555550002'),
                sms.MMSAddress(
                    charset='106',
                    type='151',
                    address='+15555550001'))))

if __name__ == '__main__':
    unittest.main()
