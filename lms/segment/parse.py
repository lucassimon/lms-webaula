# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from lms.segment.containers import *


class SegmentParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['SegmentListDTO']['SegmentDTO']
        except Exception:
            return data

        for std in ws_data:

            dt = SegmentDTO(
                lms_segment_id=int(std['LMSSegmentId']),
                description=std['Description']
            )

            if std['SegmentId']:
                dt.segment_id = int(std['SegmentId'])

            data.append(
                dt
            )

        return data
