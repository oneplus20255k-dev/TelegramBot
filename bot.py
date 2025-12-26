import os
import json
from typing import Dict, Any, Optional
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

# ============================================================
# ✅ Admin Settings
# ============================================================
ADMIN_USERNAME = "@QHGPB"
ADMIN_IDS = {8136678328}  # ✅ Chat ID للمدير

def is_admin(update: Update) -> bool:
    return update.effective_user and update.effective_user.id in ADMIN_IDS

# ============================================================
# ✅ Persistent Storage
# ============================================================
DATA_FILE = "data.json"

def load_data(default: Dict[str, Any]) -> Dict[str, Any]:
    if not os.path.exists(DATA_FILE):
        return default
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        merged = default
        merged.update(loaded)
        return merged
    except Exception:
        return default

def save_data(data: Dict[str, Any]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ============================================================
# ✅ Default Database (Universities + Colleges + Groups + Policies + Contacts)
# ============================================================
# contact:
#   phone: رقم التواصل
#   whatsapp: رقم/رابط واتساب (إن وجد)
#   email: بريد رسمي (إن وجد)
#   website: رابط صفحة الكلية/القسم إن وجد

DEFAULT_DB = {
    "dates_text": (
        "📅 *مواعيد التقديم | Application Dates*\n\n"
        "📌 سيتم تحديث المواعيد عند نزولها رسميًا.\n"
        "Will be updated once officially announced ✅"
    ),
    "universities": {
        "جامعة قطر": {
            "type": "gov",
            "abbr": "QU",
            "website": "https://www.qu.edu.qa",
            "admissions": "https://www.qu.edu.qa/en-us/students/admission/Pages/default.aspx",
            "policies": {
                "title": "لوائح جامعة قطر | QU Regulations",
                "links": [
                    ("Policy Portal | بوابة السياسات", "https://www.qu.edu.qa/en-us/about/policy/Pages/default.aspx"),
                    ("Admission & Enrollment | القبول والتسجيل", "https://www.qu.edu.qa/en-us/students/admission-and-enrollment/Pages/default.aspx"),
                ],
            },
            "groups": {"telegram": None, "whatsapp": "https://chat.whatsapp.com/CsgfPYbuYWeF2J3KI28d9X"},
            "colleges": [
                {
                    "ar": "كلية الهندسة",
                    "en": "College of Engineering",
                    "min_pct": 85,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية الطب",
                    "en": "College of Medicine",
                    "min_pct": 95,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية القانون",
                    "en": "College of Law",
                    "min_pct": 80,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية إدارة الأعمال والاقتصاد",
                    "en": "College of Business and Economics",
                    "min_pct": 80,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية الآداب والعلوم",
                    "en": "College of Arts and Sciences",
                    "min_pct": 75,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية التربية",
                    "en": "College of Education",
                    "min_pct": 75,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية الشريعة والدراسات الإسلامية",
                    "en": "College of Sharia and Islamic Studies",
                    "min_pct": 75,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية الصيدلة",
                    "en": "College of Pharmacy",
                    "min_pct": 90,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية طب الأسنان",
                    "en": "College of Dental Medicine",
                    "min_pct": 95,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
                {
                    "ar": "كلية العلوم الصحية",
                    "en": "College of Health Sciences",
                    "min_pct": 88,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {
                        "phone": "ضع رقم التواصل الرسمي",
                        "whatsapp": "ضع رقم/رابط واتساب إن وجد",
                        "email": "ضع البريد الرسمي إن وجد",
                        "website": "ضع رابط صفحة الكلية إن وجد",
                    },
                },
            ],
        },

        "جامعة لوسيل": {
            "type": "private",
            "abbr": "LU",
            "website": "https://www.lu.edu.qa",
            "admissions": "https://lu.edu.qa/admission/?lang=en",
            "policies": {
                "title": "LU Admission | قبول جامعة لوسيل",
                "links": [
                    ("Admission", "https://lu.edu.qa/admission/?lang=en"),
                    ("Admission Requirements", "https://lu.edu.qa/admission-requirements/?lang=en"),
                ],
            },
            "groups": {"telegram": "https://t.me/+ioWmf_QymsI2OGNk", "whatsapp": None},
            "colleges": [
                {
                    "ar": "كلية القانون",
                    "en": "College of Law",
                    "min_pct": 70,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None},
                },
                {
                    "ar": "كلية التجارة والأعمال",
                    "en": "College of Business",
                    "min_pct": 70,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None},
                },
                {
                    "ar": "كلية التربية والآداب",
                    "en": "College of Education & Arts",
                    "min_pct": 65,
                    "groups": {"telegram": None, "whatsapp": None},
                    "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None},
                },
            ],
        },

        "جامعة الدوحة للعلوم والتكنولوجيا": {
            "type": "private",
            "abbr": "UDST",
            "website": "https://www.udst.edu.qa",
            "admissions": "https://www.udst.edu.qa/admissions",
            "policies": {
                "title": "UDST Policies | سياسات UDST",
                "links": [
                    ("Admissions Info", "https://www.udst.edu.qa/admissions/admissions-information"),
                    ("Admissions Policy", "https://www.udst.edu.qa/about-udst/institutional-excellence-ie/policies-and-procedures/admissions-policy"),
                ],
            },
            "groups": {"telegram": None, "whatsapp": None},
            "colleges": [
                {"ar": "كلية الهندسة والتكنولوجيا", "en": "College of Engineering & Technology", "min_pct": 70,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
                {"ar": "كلية إدارة الأعمال", "en": "College of Business", "min_pct": 65,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
                {"ar": "كلية الصحة والعلوم", "en": "College of Health & Sciences", "min_pct": 70,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
                {"ar": "كلية الحوسبة وتكنولوجيا المعلومات", "en": "College of Computing & IT", "min_pct": 70,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
            ],
        },

        "جامعة حمد بن خليفة": {
            "type": "gov",
            "abbr": "HBKU",
            "website": "https://www.hbku.edu.qa",
            "admissions": "https://www.hbku.edu.qa/en/admissions",
            "policies": {
                "title": "HBKU Policies | سياسات HBKU",
                "links": [
                    ("Policies & Procedures", "https://www.hbku.edu.qa/en/office-institutional-effectiveness/policies-procedures"),
                    ("Academic Policies", "https://www.hbku.edu.qa/en/academic-policies"),
                ],
            },
            "groups": {"telegram": None, "whatsapp": None},
            "colleges": [
                {"ar": "كلية الدراسات الإسلامية", "en": "College of Islamic Studies", "min_pct": 80,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
                {"ar": "كلية العلوم والهندسة", "en": "College of Science and Engineering", "min_pct": 85,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
                {"ar": "كلية السياسات العامة", "en": "College of Public Policy", "min_pct": 80,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
                {"ar": "كلية القانون", "en": "College of Law", "min_pct": 80,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
            ],
        },

        "كلية المجتمع في قطر": {
            "type": "gov",
            "abbr": "CCQ",
            "website": "https://www.community.edu.qa",
            "admissions": "https://www.community.edu.qa/English/Admissions/Pages/default.aspx",
            "policies": {
                "title": "CCQ Admissions | قبول كلية المجتمع",
                "links": [
                    ("Admissions (EN)", "https://www.community.edu.qa/English/Admissions/Pages/default.aspx"),
                    ("Admissions (AR)", "https://www.community.edu.qa/Arabic/Admissions/Pages/New-Students.aspx"),
                ],
            },
            "groups": {"telegram": None, "whatsapp": None},
            "colleges": [
                {"ar": "برامج الدبلوم (متعددة)", "en": "Diploma Programs (Various)", "min_pct": 60,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
                {"ar": "برامج البكالوريوس (2+2)", "en": "Bachelor Programs (2+2)", "min_pct": 65,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "ضع رقم التواصل الرسمي", "whatsapp": None, "email": None, "website": None}},
            ],
        },

        "جامعات المدينة التعليمية": {
            "type": "international",
            "abbr": "QF",
            "website": "https://www.qf.org.qa",
            "admissions": "https://www.qf.org.qa/education/higher-education",
            "policies": {
                "title": "Education City | المدينة التعليمية",
                "links": [
                    ("Higher Education", "https://www.qf.org.qa/education/higher-education"),
                ],
            },
            "groups": {"telegram": None, "whatsapp": None},
            "colleges": [
                {"ar": "برامج متعددة حسب كل فرع", "en": "Varies by partner university", "min_pct": 0,
                 "groups": {"telegram": None, "whatsapp": None}, "contact": {"phone": "N/A", "whatsapp": None, "email": None, "website": None}},
            ],
        },
    }
}

DB = load_data(DEFAULT_DB)
UNIVERSITIES = DB["universities"]

# ============================================================
# ✅ Keyboards (same buttons as requested)
# ============================================================
MAIN_MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🏛️ جامعات حكومية"), KeyboardButton("🏫 جامعات أهلية/خاصة")],
        [KeyboardButton("🌍 فروع دولية داخل قطر"), KeyboardButton("🔎 بحث عن تخصص")],
        [KeyboardButton("👥 قروبات الطلاب"), KeyboardButton("📚 اللوائح والقوانين")],
        [KeyboardButton("📅 مواعيد التقديم"), KeyboardButton("ℹ️ عن البوت")],
    ],
    resize_keyboard=True
)

def build_universities_keyboard(kind: str) -> ReplyKeyboardMarkup:
    buttons = []
    names = [u for u, data in UNIVERSITIES.items() if data.get("type") == kind]
    for name in names:
        buttons.append([KeyboardButton(name)])
    buttons.append([KeyboardButton("⬅️ رجوع")])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

GOV_MENU = build_universities_keyboard("gov")
PRIVATE_MENU = build_universities_keyboard("private")
INTERNATIONAL_MENU = build_universities_keyboard("international")

def build_colleges_keyboard(university_name: str) -> ReplyKeyboardMarkup:
    colleges = UNIVERSITIES[university_name]["colleges"]
    rows = [[KeyboardButton(c["ar"])] for c in colleges]
    rows.append([KeyboardButton("⬅️ رجوع للجامعات")])
    rows.append([KeyboardButton("🏠 القائمة الرئيسية")])
    return ReplyKeyboardMarkup(rows, resize_keyboard=True)

# ============================================================
# ✅ Texts
# ============================================================
WELCOME_TEXT = (
    "🎓 *بوت خريجي الثانوية – قطر 🇶🇦*\n\n"
    "✅ جامعات | Universities\n"
    "✅ كليات + نسب | Colleges + %\n"
    "✅ قروبات | Groups\n"
    "✅ لوائح | Policies\n"
    "✅ تواصل الكليات | College Contact\n\n"
    "📌 اختر من القائمة 👇"
)

ABOUT_TEXT = (
    "ℹ️ *عن البوت | About*\n\n"
    "بوت إرشادي لخريجي الثانوية في قطر.\n"
    "Guidance bot for Qatar universities.\n\n"
    f"👤 Admin: {ADMIN_USERNAME}"
)

GROUPS_TEXT = (
    "👥 *قروبات الطلاب | Student Groups*\n\n"
    "📌 ادخل الجامعة ثم اختر (👥 قروبات الجامعة).\n"
    "Go to a university, then choose (University Groups).\n\n"
    f"👤 Admin: {ADMIN_USERNAME}"
)

SEARCH_HINT = (
    "🔎 *بحث عن تخصص | Major Search*\n\n"
    "اكتب اسم التخصص الآن (مثال: هندسة، طب، قانون...)\n"
    "Type a major (e.g., Engineering, Medicine, Law) ✅"
)

USER_STATE = {}
USER_CTX = {}

def build_law_text() -> str:
    lines = ["📚 *اللوائح والقوانين | Policies*\n"]
    lines.append("✅ روابط رسمية (Official Links):\n")
    for uni, data in UNIVERSITIES.items():
        pol = data.get("policies", {})
        links = pol.get("links", [])
        if not links:
            continue
        lines.append(f"🏛️ *{uni}*")
        title = pol.get("title", "")
        if title:
            lines.append(f"📌 {title}")
        for name, url in links:
            lines.append(f"• {name}: {url}")
        lines.append("")
    lines.append("📌 المرجع النهائي هو موقع الجامعة.")
    return "\n".join(lines)

# ============================================================
# ✅ Simple Major DB
# ============================================================
MAJORS_DB = {
    "طب": ["جامعة قطر — كلية الطب — https://www.qu.edu.qa/en-us/students/admission/Pages/default.aspx"],
    "هندسة": ["جامعة قطر — كلية الهندسة — https://www.qu.edu.qa/en-us/students/admission/Pages/default.aspx"],
    "قانون": [
        "جامعة قطر — كلية القانون — https://www.qu.edu.qa/en-us/students/admission/Pages/default.aspx",
        "جامعة لوسيل — كلية القانون — https://lu.edu.qa/admission/?lang=en",
    ],
}

def find_college(uni_name: str, college_ar: str) -> Optional[Dict[str, Any]]:
    uni = UNIVERSITIES.get(uni_name)
    if not uni:
        return None
    for c in uni.get("colleges", []):
        if c.get("ar") == college_ar:
            return c
    return None

# ============================================================
# ✅ Admin Commands
# ============================================================
async def admin_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("❌ Admin only.\n👤 Admin: " + ADMIN_USERNAME)
        return

    msg = (
        "🛠️ *لوحة المدير | Admin Panel*\n\n"
        "✅ تحديث قروب جامعة:\n"
        "`/set_uni_group <اسم الجامعة> <telegram|whatsapp> <link|none>`\n\n"
        "✅ تحديث قروب كلية:\n"
        "`/set_college_group <اسم الجامعة> <اسم الكلية> <telegram|whatsapp> <link|none>`\n\n"
        "✅ تحديث نسبة قبول كلية:\n"
        "`/set_pct <اسم الجامعة> <اسم الكلية> <النسبة>`\n\n"
        "✅ تحديث مواعيد التقديم:\n"
        "`/set_dates النص هنا...`\n\n"
        "✅ عرض المواعيد:\n"
        "`/show_dates`\n"
    )
    await update.message.reply_text(msg, parse_mode="Markdown")

async def set_uni_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("❌ Admin only.")
        return
    if len(context.args) < 3:
        await update.message.reply_text("❌ /set_uni_group <uni> <telegram|whatsapp> <link|none>")
        return

    link = context.args[-1].strip()
    kind = context.args[-2].strip().lower()
    uni_name = " ".join(context.args[:-2]).strip()

    if uni_name not in UNIVERSITIES:
        await update.message.reply_text("❌ الجامعة غير موجودة.")
        return
    if kind not in ("telegram", "whatsapp"):
        await update.message.reply_text("❌ النوع لازم telegram أو whatsapp.")
        return

    UNIVERSITIES[uni_name]["groups"][kind] = None if link.lower() == "none" else link
    DB["universities"] = UNIVERSITIES
    save_data(DB)
    await update.message.reply_text(f"✅ تم تحديث قروب الجامعة: {uni_name} ({kind})")

async def set_college_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("❌ Admin only.")
        return
    if len(context.args) < 4:
        await update.message.reply_text("❌ /set_college_group <uni> <college> <telegram|whatsapp> <link|none>")
        return

    link = context.args[-1].strip()
    kind = context.args[-2].strip().lower()
    joined = " ".join(context.args[:-2]).strip()

    matched_uni = None
    for uni_name in UNIVERSITIES.keys():
        if joined.startswith(uni_name):
            matched_uni = uni_name
            break
    if not matched_uni:
        await update.message.reply_text("❌ لم أستطع تحديد الجامعة.")
        return

    college_ar = joined.replace(matched_uni, "", 1).strip()
    c = find_college(matched_uni, college_ar)
    if not c:
        await update.message.reply_text("❌ الكلية غير موجودة.")
        return
    if kind not in ("telegram", "whatsapp"):
        await update.message.reply_text("❌ النوع لازم telegram أو whatsapp.")
        return

    if "groups" not in c:
        c["groups"] = {"telegram": None, "whatsapp": None}
    c["groups"][kind] = None if link.lower() == "none" else link

    DB["universities"] = UNIVERSITIES
    save_data(DB)
    await update.message.reply_text(f"✅ تم تحديث قروب الكلية: {matched_uni} — {college_ar} ({kind})")

async def set_pct(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("❌ Admin only.")
        return
    if len(context.args) < 3:
        await update.message.reply_text("❌ /set_pct <uni> <college> <pct>")
        return

    try:
        pct = int(context.args[-1].strip())
        if pct < 0 or pct > 100:
            raise ValueError
    except ValueError:
        await update.message.reply_text("❌ النسبة يجب أن تكون 0 إلى 100.")
        return

    joined = " ".join(context.args[:-1]).strip()
    matched_uni = None
    for uni_name in UNIVERSITIES.keys():
        if joined.startswith(uni_name):
            matched_uni = uni_name
            break
    if not matched_uni:
        await update.message.reply_text("❌ لم أستطع تحديد الجامعة.")
        return

    college_ar = joined.replace(matched_uni, "", 1).strip()
    c = find_college(matched_uni, college_ar)
    if not c:
        await update.message.reply_text("❌ الكلية غير موجودة.")
        return

    c["min_pct"] = pct
    DB["universities"] = UNIVERSITIES
    save_data(DB)
    await update.message.reply_text(f"✅ تم تحديث نسبة القبول: {matched_uni} — {college_ar} = {pct}%")

async def set_dates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("❌ Admin only.")
        return
    new_text = update.message.text.replace("/set_dates", "", 1).strip()
    if not new_text:
        await update.message.reply_text("❌ اكتب النص بعد الأمر.")
        return
    DB["dates_text"] = new_text
    save_data(DB)
    await update.message.reply_text("✅ تم تحديث مواعيد التقديم.")

async def show_dates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("❌ Admin only.")
        return
    await update.message.reply_text(DB.get("dates_text", ""), parse_mode="Markdown")

# ============================================================
# ✅ Basic Commands
# ============================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    USER_STATE.pop(chat_id, None)
    USER_CTX.pop(chat_id, None)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=MAIN_MENU, parse_mode="Markdown")

async def show_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    USER_STATE.pop(chat_id, None)
    USER_CTX.pop(chat_id, None)
    await update.message.reply_text("✅ رجعت للقائمة الرئيسية | Back to main", reply_markup=MAIN_MENU)

# ============================================================
# ✅ Message Handler
# ============================================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text.strip()

    if text == "🏠 القائمة الرئيسية":
        await show_main(update, context)
        return

    if text == "⬅️ رجوع":
        await show_main(update, context)
        return

    if text == "⬅️ رجوع للجامعات":
        last_menu = (USER_CTX.get(chat_id) or {}).get("last_menu")
        if last_menu == "gov":
            await update.message.reply_text("🏛️ اختر جامعة حكومية:", reply_markup=GOV_MENU)
        elif last_menu == "private":
            await update.message.reply_text("🏫 اختر جامعة أهلية/خاصة:", reply_markup=PRIVATE_MENU)
        elif last_menu == "international":
            await update.message.reply_text("🌍 اختر:", reply_markup=INTERNATIONAL_MENU)
        else:
            await show_main(update, context)
        return

    # ====== Menus ======
    if text == "🏛️ جامعات حكومية":
        USER_STATE.pop(chat_id, None)
        USER_CTX[chat_id] = {"last_menu": "gov"}
        await update.message.reply_text("🏛️ اختر جامعة حكومية:", reply_markup=GOV_MENU)
        return

    if text == "🏫 جامعات أهلية/خاصة":
        USER_STATE.pop(chat_id, None)
        USER_CTX[chat_id] = {"last_menu": "private"}
        await update.message.reply_text("🏫 اختر جامعة أهلية/خاصة:", reply_markup=PRIVATE_MENU)
        return

    if text == "🌍 فروع دولية داخل قطر":
        USER_STATE.pop(chat_id, None)
        USER_CTX[chat_id] = {"last_menu": "international"}
        await update.message.reply_text("🌍 اختر:", reply_markup=INTERNATIONAL_MENU)
        return

    if text == "👥 قروبات الطلاب":
        USER_STATE.pop(chat_id, None)
        await update.message.reply_text(GROUPS_TEXT, reply_markup=MAIN_MENU, parse_mode="Markdown")
        return

    if text == "📚 اللوائح والقوانين":
        USER_STATE.pop(chat_id, None)
        await update.message.reply_text(build_law_text(), reply_markup=MAIN_MENU, parse_mode="Markdown")
        return

    if text == "📅 مواعيد التقديم":
        USER_STATE.pop(chat_id, None)
        await update.message.reply_text(DB.get("dates_text", ""), reply_markup=MAIN_MENU, parse_mode="Markdown")
        return

    if text == "ℹ️ عن البوت":
        USER_STATE.pop(chat_id, None)
        await update.message.reply_text(ABOUT_TEXT, reply_markup=MAIN_MENU, parse_mode="Markdown")
        return

    # ====== University Page ======
    if text in UNIVERSITIES:
        uni = text
        USER_STATE.pop(chat_id, None)
        USER_CTX.setdefault(chat_id, {})
        USER_CTX[chat_id]["university"] = uni

        data = UNIVERSITIES[uni]
        groups = data.get("groups", {})
        tg = groups.get("telegram")
        wa = groups.get("whatsapp")

        tg_line = tg if tg else "N/A"
        wa_line = wa if wa else "N/A"

        msg = (
            f"🏛️ *{uni}* ({data.get('abbr','')})\n\n"
            f"🌐 Website:\n{data.get('website')}\n\n"
            f"📝 Admissions:\n{data.get('admissions')}\n\n"
            f"👥 Uni Groups:\n"
            f"• Telegram: {tg_line}\n"
            f"• WhatsApp: {wa_line}\n\n"
            f"📌 اختر خدمة | Choose:\n"
        )

        uni_keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("🏫 الكليات / Colleges"), KeyboardButton("👥 قروبات الجامعة / University Groups")],
                [KeyboardButton("⬅️ رجوع للجامعات"), KeyboardButton("🏠 القائمة الرئيسية")],
            ],
            resize_keyboard=True
        )
        await update.message.reply_text(msg, reply_markup=uni_keyboard, parse_mode="Markdown")
        return

    # ====== University Groups ======
    if text == "👥 قروبات الجامعة / University Groups":
        uni = (USER_CTX.get(chat_id) or {}).get("university")
        if not uni or uni not in UNIVERSITIES:
            await update.message.reply_text("❌ اختر جامعة أولاً.", reply_markup=MAIN_MENU)
            return

        groups = UNIVERSITIES[uni].get("groups", {})
        tg = groups.get("telegram")
        wa = groups.get("whatsapp")

        tg_line = tg if tg else "غير متوفر | N/A"
        wa_line = wa if wa else "غير متوفر | N/A"

        msg = (
            f"👥 *University Groups | قروبات الجامعة*\n\n"
            f"🏛️ *{uni}*\n\n"
            f"📱 Telegram:\n{tg_line}\n\n"
            f"🟢 WhatsApp:\n{wa_line}\n\n"
            f"👤 Admin: {ADMIN_USERNAME}"
        )

        uni_keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("🏫 الكليات / Colleges"), KeyboardButton("👥 قروبات الجامعة / University Groups")],
                [KeyboardButton("⬅️ رجوع للجامعات"), KeyboardButton("🏠 القائمة الرئيسية")],
            ],
            resize_keyboard=True
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=uni_keyboard)
        return

    # ====== Colleges ======
    if text == "🏫 الكليات / Colleges":
        uni = (USER_CTX.get(chat_id) or {}).get("university")
        if not uni or uni not in UNIVERSITIES:
            await update.message.reply_text("❌ اختر جامعة أولاً.", reply_markup=MAIN_MENU)
            return

        kb = build_colleges_keyboard(uni)
        await update.message.reply_text(f"🏫 كليات {uni}:", reply_markup=kb)
        return

    # ====== College Details (adds contacts)
    uni = (USER_CTX.get(chat_id) or {}).get("university")
    if uni and uni in UNIVERSITIES:
        for c in UNIVERSITIES[uni]["colleges"]:
            if text == c.get("ar"):
                min_pct = c.get("min_pct", 0)
                pct_line = "غير محددة | N/A" if min_pct == 0 else f"{min_pct}% (approx.)"

                cg = c.get("groups", {})
                tg = cg.get("telegram")
                wa = cg.get("whatsapp")
                tg_line = tg if tg else "N/A"
                wa_line = wa if wa else "N/A"

                contact = c.get("contact", {})
                phone = contact.get("phone", "N/A")
                cwa = contact.get("whatsapp", "N/A")
                email = contact.get("email", "N/A")
                website = contact.get("website", "N/A")

                msg = (
                    f"🏫 *{c['ar']}*\n"
                    f"🎓 {c.get('en','')}\n\n"
                    f"📊 Min %: {pct_line}\n\n"
                    f"👥 College Groups:\n"
                    f"• Telegram: {tg_line}\n"
                    f"• WhatsApp: {wa_line}\n\n"
                    f"📞 Contact:\n"
                    f"• Phone: {phone}\n"
                    f"• WhatsApp: {cwa}\n"
                    f"• Email: {email}\n"
                    f"• Page: {website}\n\n"
                    f"📌 Note: Admission changes yearly."
                )

                await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=build_colleges_keyboard(uni))
                return

    # ====== Search ======
    if text == "🔎 بحث عن تخصص":
        USER_STATE[chat_id] = "SEARCH"
        await update.message.reply_text(SEARCH_HINT, reply_markup=MAIN_MENU, parse_mode="Markdown")
        return

    if USER_STATE.get(chat_id) == "SEARCH":
        major = text
        results = MAJORS_DB.get(major)
        if results:
            msg = "✅ *Results | نتائج:*\n\n" + "\n".join(f"• {r}" for r in results)
        else:
            msg = "❌ Not found.\n📌 جرّب: طب / هندسة / قانون ✅"
        await update.message.reply_text(msg, reply_markup=MAIN_MENU, parse_mode="Markdown")
        return

    await update.message.reply_text("❓ اختر من الأزرار أو اكتب /start ✅", reply_markup=MAIN_MENU)

# ============================================================
# ✅ Main
# ============================================================
def main():
    if not TOKEN:
        print("❌ BOT_TOKEN غير موجود. ضع التوكن ثم شغّل.")
        return

    app = Application.builder().token(TOKEN).build()

    # Public
    app.add_handler(CommandHandler("start", start))

    # Admin
    app.add_handler(CommandHandler("admin", admin_help))
    app.add_handler(CommandHandler("set_uni_group", set_uni_group))
    app.add_handler(CommandHandler("set_college_group", set_college_group))
    app.add_handler(CommandHandler("set_pct", set_pct))
    app.add_handler(CommandHandler("set_dates", set_dates))
    app.add_handler(CommandHandler("show_dates", show_dates))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ البوت شغال... افتح تيليجرام وجرب /start")
    app.run_polling()

if __name__ == "__main__":
    main()
