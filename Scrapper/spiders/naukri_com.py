from __future__ import absolute_import

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from ..items import PortiaItem, HiringItem
from ..utils.processors import Item, Field
from ..utils.spiders import BasePortiaSpider


class Naukri(BasePortiaSpider):
    name = "naukri"
    allowed_domains = [u'www.naukri.com']
    start_urls = [u'https://www.naukri.com/recruiters-in-bangalore-1']
    rules = [
        Rule(
            LinkExtractor(
                tags=['link'],
                attrs=['href'],
                restrict_css='link[rel=next]',
                deny=()
            ),
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow=(u'https://www.naukri.com/recruiters/*'),
                deny=()
            ),
            callback='parse_item',
            follow=False
        )
    ]
    items = [
        [
            Item(PortiaItem,
                 None,
                 u'body > .wrap',
                 [Field(u'profile_image',
                        '.imgWrapper > .fl::attr(src)',
                        []),
                  Field(u'name',
                        '.infoWrapper > .mt10 > .fl *::text',
                        []),
                  Field(u'designation',
                        '.infoWrapper > .ellipsis *::text',
                        []),
                  Field(u'company',
                        '.infoWrapper > div:nth-child(4) *::text',
                        []),
                  Field(u'location',
                        '.infoWrapper > div:nth-child(5) *::text',
                        []),
                  Field(u'active_jobs',
                        '.infoWrapper > .activeJobs *::text',
                        []),

                  Field(u'about',
                        '.infoWrapper > .mltiLnElps *::text',
                        []),
                  Field(u'skills',
                        '.info > #skillInfo > p:nth-of-type(1) *::text',
                        []),
                  Field(u'levels',
                        '.info > #skillInfo > p:nth-of-type(2) *::text',
                        []),
                  Field(u'functional_areas',
                        '.info > #skillInfo > p:nth-of-type(3) *::text',
                        []),
                  Field(u'industries',
                        '.info > #skillInfo > p:nth-of-type(4) *::text',
                        []),

                  Field(u'current_company',
                        '.info > #workInfo > p:nth-of-type(1) *::text',
                        []),
                  Field(u'current_designation',
                        '.info > #workInfo > p:nth-of-type(2) *::text',
                        []),
                  Field(u'current_job_profile',
                        '.info > #workInfo > p:nth-of-type(3) *::text',
                        []),
                  Field(u'role_in_hiring',
                        '.info > #workInfo > p:nth-of-type(4) *::text',
                        []),

                  Field(u'previous_company',
                        '.info > #workInfo > .hDvdr > p:nth-of-type(1) *::text',
                        []),
                  Field(u'previous_designation',
                        '.info > #workInfo > .hDvdr > p:nth-of-type(2) *::text',
                        []),
                  Field(u'previous_job_profile',
                        '.info > #workInfo > .hDvdr > p:nth-of-type(3) *::text',
                        []),

                  Item(HiringItem,
                       u'currently_hiring',
                       u'#tabJ-1 > .hrngInfo > li',
                       [Field(u'page_link',
                              '.f14::attr(href)',
                              []),
                        Field(u'title',
                              '.f14 *::text',
                              []),
                        Field(u'company',
                              'p *::text',
                              []),
                        Field(u'experience',
                              '.oh > span:nth-child(1) > .exp *::text',
                              []),
                        Field(u'location',
                              '.oh > span:nth-child(2) > .fl *::text',
                              [])]),
                  Item(HiringItem,
                       u'positions_managed',
                       u'#tabJ-2 > .hrngInfo > li',
                       [Field(u'page_link',
                              '.f14::attr(href)',
                              []),
                        Field(u'title',
                              '.f14 *::text',
                              []),
                        Field(u'company',
                              'p *::text',
                              []),
                        Field(u'experience',
                              '.oh > span:nth-child(1) > .exp *::text',
                              []),
                        Field(u'location',
                              '.oh > span:nth-child(2) > .loc *::text',
                              [])])

                  ]
                 )

        ]
    ]
