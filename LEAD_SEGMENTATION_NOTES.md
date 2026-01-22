# Lead Segmentation Notes

## Goal
Find 10-20 design partner candidates for Hoop (AI chat support tool) from a list of 1,013 Shopify brand leads.

## Strategy
Target brands that:
- Do NOT have an existing chat tool (greenfield opportunity, no switching cost)
- Are 2-5 years old (agile, likely still founder-led)

## Data Source
- **File**: `leads_1000_shopify_brands.csv`
- **Total brands**: 1,013
- **Source**: Various D2C directories, Shopify features, industry lists

## Column Analysis
| Column | Fill Rate | Notes |
|--------|-----------|-------|
| brand_name, category, subcategory, website | 100% | Core data |
| founded_year, headquarters, description | 100% | Good for filtering |
| source | 100% | D2C directory (567), D2C leader (163), Industry list (98) |
| chat_widget | 18% | Only 187 have data (87 Yes, 100 No, 826 unknown) |
| founder_1, linkedin_1 | 12% | Partially enriched (~120 brands) |
| employee_count | 3% | Very sparse (33 brands) |

## Filtering Process
```
1,013 total brands
  → 926 without confirmed chat tool (chat_widget != 'Yes')
  → 17 founded 2021-2024 (2-5 years old)
```

## Segment bs001 (17 brands)
Brands tagged with `segment_id = bs001`:

| Brand | Year | Category |
|-------|------|----------|
| Almave | 2023 | Non-Alcoholic |
| Graza | 2022 | Oils |
| Namesake | 2022 | Skincare |
| Threaded | 2022 | Bedding |
| HYTE | 2022 | PC |
| Popsmith | 2021 | Popcorn |
| Figlia | 2021 | Non-Alcoholic |
| Nello | 2021 | Wellness Drinks |
| Laundry Sauce | 2021 | Laundry |
| Ciriaco | 2021 | Bags |
| Made by Nacho | 2021 | Cat Food |
| Marin Instruments | 2021 | Watches |
| Vacation Inc | 2021 | Sunscreen |
| Henry Meds | 2021 | Telehealth |
| August | 2021 | Period |
| August | 2021 | Intimacy |
| Everyday Dose | 2021 | Mushroom |

## Files Created/Modified
- `leads_1000_shopify_brands.csv` - Added columns: `has_contact_info`, `contacted`, `segment_id`
- `leads_segment_bs001.csv` - Subset of 17 brands in segment bs001

## Next Steps
- Research each brand in bs001 segment
- Find founder contact info (LinkedIn, email)
- Prepare personalized outreach

## Future Segments to Consider
- Brands currently using Gorgias (to understand competitor experience)
- Larger established brands (different value prop)
- Specific high-support categories (supplements, skincare)
