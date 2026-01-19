# knowledge_base.py
# Punjab Business Finance Scheme Knowledge Base in Urdu

URDU_KB = {
    "scheme_info": {
        "name": "سی ایم پنجاب آسان کاروبار فنانس اسکیم",
        "description": "یہ اسکیم پنجاب کے چھوٹے اور درمیانے درجے کے کاروباری حضرات کو مالی معاونت فراہم کرنے کے لیے ڈیزائن کی گئی ہے تاکہ وہ اپنے کاروبار کو قائم اور بڑھا سکیں۔",
        "objectives": [
            "روزگار کے مواقع پیدا کرنا",
            "برآمدات کو فروغ دینا",
            "صوبے کی اقتصادی ترقی کو بڑھانا"
        ],
        "partners": "حکومت پنجاب (GoPb) اور بینک آف پنجاب (BOP)"
    },
    
    "financing_purposes": [
        "نئے کاروبار کے قیام کے لیے",
        "BMR (توازن، جدید کاری اور تبدیلی)",
        "موجودہ کاروبار کی توسیع",
        "ورکنگ کیپیٹل",
        "تجارتی لاجسٹکس کے لیے لیز"
    ],
    
    "target_sectors": "تمام شعبے، بشمول زرعی SME، جیسا کہ SBP کے Prudential Regulations میں ذکر ہے",
    
    "loan_tiers": {
        "TIER-1": {
            "amount_range": "5 ملین روپے سے 30 ملین روپے",
            "category": "صرف درمیانے کاروبار (ME)",
            "security_type": "محفوظ شدہ سیکیورٹی",
            "processing": "BOP کے کریڈٹ انڈر رائٹنگ کے معیار کے مطابق کیس بہ کیس",
            "interest_rate": "0%",
            "payment": "ماہانہ مساوی قسطیں",
            "loan_tenure": "زیادہ سے زیادہ 5 سال (گریس پیریڈ حسب ضرورت)",
            "processing_fee": "5,000 روپے",
            "equity_required": "0% (لیز شدہ تجارتی گاڑی کے عالوہ) / 25% (لیز شدہ گاڑی)",
            "dbr_limit": "ماہانہ خالص آمدنی کا 40% تک"
        },
        
        "TIER-2": {
            "amount_range": "1 ملین روپے سے 5 ملین روپے",
            "category": "چھوٹے اور درمیانے کاروبار (SE & ME)",
            "security_type": "صرف ذاتی ضمانت",
            "processing": "BOP کے Statistical Scoring ماڈل کے ذریعے مکمل ڈیجیٹل",
            "interest_rate": "0%",
            "payment": "ماہانہ مساوی قسطیں",
            "loan_tenure": "زیادہ سے زیادہ 5 سال (نئے کاروبار کے لیے 6 ماہ تک گریس پیریڈ، موجودہ کاروبار کے لیے 3 ماہ تک)",
            "processing_fee": "10,000 روپے",
            "equity_required": "20% (دیگر تمام معاملات میں) / 10% (خواتین، ٹرانسجینڈر اور معذور افراد)",
            "dbr_limit": "ماہانہ خالص آمدنی کا 50% تک"
        }
    },
    
    "security_requirements": {
        "TIER-1": [
            "درخواست گزار / شراکت دار / ڈائریکٹر کی ذاتی ضمانتیں",
            "ذاتی نیٹ ورتھ اسٹیٹمنٹ کی کاپیاں (FBR کے ساتھ فائل شدہ ترجیحی)"
        ],
        "TIER-2": [
            "رہائشی / تجارتی / صنعتی پراپرٹی کی رہن (BOP پالیسی کے مطابق)",
            "یا کوئی اور قابل قبول سیکیورٹی BOP کی صوابدید پر"
        ],
        "vehicle_financing": "مقامی طور پر تیار شدہ / اسمبل شدہ گاڑی خود سیکیورٹی کے طور پر کافی ہوگی اور BOP کے نام پر رجسٹر ہوگی"
    },
    
    "charges": {
        "insurance": "بنیادی سیکیورٹی (پراپرٹی / لیز شدہ اثاثہ / اسٹاک) کا مکمل انشورنس ضروری ہے",
        "other_charges": "ویلیوئیشن، قانونی، دستاویزات، رہن رجسٹریشن، دوبارہ قبضہ، اسٹاک ہینڈلنگ، مکردم، ریونیو اسٹامپس اور حکومتی فیسیں حقیقی اخراجات پر",
        "handling_fee_new_business": "کوئی فیس نہیں",
        "handling_fee_bmr": "3% سالانہ",
        "handling_fee_green": "ماحول دوست کاروبار کے لیے کوئی فیس نہیں",
        "late_payment_charges": "1 روپے روزانہ فی 1,000 روپے بنیادی رقم پر",
        "loan_price": "6 ماہ کی اوسط KIBOR + 2.40% سالانہ"
    },
    
    "payment_details": {
        "payment_mode": "مساوی ماہانہ قسطیں",
        "payment_date": "ہر ماہ 1 تاریخ",
        "first_installment_TIER1": {
            "before_15th": "اگلے ماہ کی 1 تاریخ",
            "after_15th": "دوسرے ماہ کی 1 تاریخ"
        }
    },
    
    "eligibility_criteria": {
        "business_type": "چھوٹے اور درمیانے کاروبار (SMEs) SBP کے مطابق",
        "ownership_TIER1": "واحد ملکیت (Sole Proprietorship)",
        "fdr_registration": "FBR میں رجسٹرڈ اور ٹیکس ادا کرنے والا",
        "age": "25 سے 55 سال",
        "citizenship": "پاکستانی شہری، CNIC کے ساتھ پنجاب میں مقیم",
        "business_location": "پنجاب",
        "one_loan_per_business": "ہر کاروبار کے لیے ایک قرض فی جگہ",
        "credit_history": "صاف ECIB / کریڈٹ ہسٹری",
        "ntn_cnic_validity": "NTN اور CNIC کی درستگی",
        "bop_sbp_compliance": "BOP اور SBP کے معیار کے مطابق",
        "business_location_requirement": "ورکنگ کیپیٹل، توسیع، اور BMR کے لیے کاروبار کی جگہ ملکیت یا کرایہ پر ہونی چاہیے"
    },
    
    "equity_requirements": {
        "TIER1_vehicle_leasing": "0% (لیز شدہ تجارتی گاڑی کے عالوہ)",
        "TIER1_vehicle": "کم از کم 25% پیشگی جمع کروانا ضروری",
        "TIER2_general": "20% ایکویٹی دیگر تمام معاملات میں",
        "TIER2_special": "10% ایکویٹی (خواتین، ٹرانسجینڈر اور معذور افراد کے لیے CNIC یا معذوری سرٹیفکیٹ کے ساتھ)",
        "minimum_all_loans": "تمام قرضوں میں کم از کم 25% ایکویٹی ضروری ہے",
        "equity_form": "نقد رقم یا غیر منقولہ جائیداد کی صورت میں",
        "equity_timing": "قرض کی ادائیگی سے پہلے جمع کرانی ہوگی"
    },
    
    "faq": [
        {
            "question": "یہ اسکیم کیا ہے؟",
            "answer": "سی ایم پنجاب آسان کاروبار فنانس اسکیم ایک حکومتی اسکیم ہے جو پنجاب میں چھوٹے اور درمیانے کاروباری حضرات کو مالی معاونت فراہم کرتی ہے تاکہ وہ اپنے کاروبار کو قائم اور بڑھا سکیں۔"
        },
        {
            "question": "قرض کی رقم کتنی ہے؟",
            "answer": "درمیانے کاروبار کے لیے 5 ملین روپے سے 30 ملین روپے اور چھوٹے کاروبار کے لیے 1 ملین روپے سے 5 ملین روپے۔"
        },
        {
            "question": "سود کی شرح کیا ہے؟",
            "answer": "0% سود ہے۔ لیکن قرض کی قیمت میں 6 ماہ کی اوسط بینک ریٹ اور 2.40% سالانہ شامل ہے۔"
        },
        {
            "question": "کون اس اسکیم کے لیے اہل ہے؟",
            "answer": "پاکستانی شہری، 25 سے 55 سال، محصول اور آمدنی بورڈ میں رجسٹرڈ اور ٹیکس ادا کرنے والا، صاف کریڈٹ ہسٹری والا، اور پنجاب میں مقیم ہونا ضروری ہے۔"
        },
        {
            "question": "ایکویٹی کتنی ہونی چاہیے؟",
            "answer": "چھوٹے کاروبار کے لیے عام طور پر 20% ہے لیکن خواتین، ٹرانسجینڈر اور معذور افراد کے لیے 10% ہے۔ درمیانے کاروبار کے لیے شرائط مختلف ہیں۔"
        },
        {
            "question": "قرض کی ادائیگی کی مدت کیا ہے؟",
            "answer": "زیادہ سے زیادہ 5 سال۔ نئے کاروبار کے لیے 6 ماہ تک معافی کی مدت اور موجودہ کاروبار کے لیے 3 ماہ تک معافی کی مدت ہے۔"
        },
        {
            "question": "کون سی حکومتیں اس اسکیم میں حصہ دار ہیں؟",
            "answer": "حکومت پنجاب اور بینک آف پنجاب اس اسکیم کو مل کر چلاتے ہیں۔ حکومت نشان زد سبسڈی فراہم کرتی ہے۔"
        },
        {
            "question": "ادائیگی کی تفصیلات کیا ہیں؟",
            "answer": "ادائیگی ماہانہ مساوی قسطوں میں ہوتی ہے۔ پہلی قسط کی تاریخ بکنگ کی تاریخ پر منحصر ہے۔ تاخیری ادائیگی پر 1 روپے روزانہ فی 1,000 روپے چارج ہے۔"
        },
        {
            "question": "سیکیورٹی کی ضروریات کیا ہیں؟",
            "answer": "درمیانے کاروبار کے لیے شناخت اور رہائش کے کاغذات ضروری ہیں۔ چھوٹے کاروبار کے لیے پراپرٹی یا دوسری قابل قبول سیکیورٹی رکھی جاتی ہے۔"
        }
    ]
}

def search_kb(query: str, top_results: int = 3) -> list:
    """
    Search knowledge base for relevant information
    Returns list of relevant results
    """
    query_lower = query.lower()
    results = []
    
    # Search in FAQ
    for faq in URDU_KB.get("faq", []):
        if query_lower in faq["question"].lower() or query_lower in faq["answer"].lower():
            results.append({
                "type": "FAQ",
                "question": faq["question"],
                "answer": faq["answer"]
            })
    
    # Search in financing purposes
    for purpose in URDU_KB.get("financing_purposes", []):
        if query_lower in purpose.lower():
            results.append({
                "type": "مقصد",
                "content": purpose
            })
    
    # Search in eligibility criteria
    for key, value in URDU_KB.get("eligibility_criteria", {}).items():
        if isinstance(value, str) and query_lower in value.lower():
            results.append({
                "type": "اہلیت",
                "criterion": key,
                "detail": value
            })
    
    return results[:top_results]

def get_kb_summary(tier: str = None) -> str:
    """
    Get summary of scheme for LLM context
    """
    scheme_name = URDU_KB["scheme_info"]["name"]
    description = URDU_KB["scheme_info"]["description"]
    
    if tier == "TIER-1":
        tier_info = URDU_KB["loan_tiers"]["TIER-1"]
        return f"""
{scheme_name}

{description}

TIER-1 معلومات:
- قرض کی رقم: {tier_info['amount_range']}
- شرح: {tier_info['interest_rate']}
- پروسیسنگ فیس: {tier_info['processing_fee']}
- ایکویٹی: {tier_info['equity_required']}
- قرض کی مدت: {tier_info['loan_tenure']}
"""
    
    elif tier == "TIER-2":
        tier_info = URDU_KB["loan_tiers"]["TIER-2"]
        return f"""
{scheme_name}

{description}

TIER-2 معلومات:
- قرض کی رقم: {tier_info['amount_range']}
- شرح: {tier_info['interest_rate']}
- پروسیسنگ فیس: {tier_info['processing_fee']}
- ایکویٹی: {tier_info['equity_required']}
- قرض کی مدت: {tier_info['loan_tenure']}
"""
    
    else:
        return f"""
{scheme_name}

{description}

مقاصد:
{', '.join(URDU_KB['scheme_info']['objectives'])}

فنانسنگ کے مقاصد:
{', '.join(URDU_KB['financing_purposes'])}
"""

def get_eligibility_summary() -> str:
    """Get eligibility criteria summary"""
    criteria = URDU_KB["eligibility_criteria"]
    summary = "اہلیت کے معیار:\n"
    for key, value in criteria.items():
        summary += f"• {value}\n"
    return summary

def format_kb_for_llm(query: str) -> str:
    """
    Format KB data for injection into LLM prompt
    """
    search_results = search_kb(query)
    kb_context = get_kb_summary()
    
    formatted = f"""
دستاویز کی معلومات:
{kb_context}

صارف کے سوال سے متعلق معلومات:
"""
    
    if search_results:
        for i, result in enumerate(search_results, 1):
            if result["type"] == "FAQ":
                formatted += f"\n{i}. سوال: {result['question']}\nجواب: {result['answer']}"
            else:
                formatted += f"\n{i}. {result.get('content', str(result))}"
    
    return formatted
