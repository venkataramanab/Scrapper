from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image, BaseProcessor


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class HiringItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join()
    )
    company = scrapy.Field(
        input_processor=Text(),
        output_processor=Join()
    )
    experience = scrapy.Field(
        input_processor=Text(),
        output_processor=Join()
    )

    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join()
    )

    page_link = scrapy.Field(
        input_processot=Url(),
        output_processor=Join()
    )


class SharonHrManagerInBarelogicSolutionsPrivateItem(PortiaItem):
    name = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    designation = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    active_jobs = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    location = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    company = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    profile_image = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    about = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    skills = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    levels = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    functional_areas = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    industries = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )

    current_company = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    current_designation = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    current_job_profile = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )

    previous_company = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    previous_designation = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    previous_job_profile = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )

    role_in_hiring = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    page_link = scrapy.Field(
        input_processor=Url(),
        output_processor=Join()
    )

    currently_hiring = scrapy.Field()
    positions_managed = scrapy.Field()
