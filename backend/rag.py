import os
from langchain_groq import ChatGroq

class RAGEngine:
    def __init__(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.knowledge_context = f.read()
        except Exception as e:
            self.knowledge_context = ""
            print(f"Warning: Could not read knowledge base. {e}")

        self.llm = None
        
        # Comprehensive knowledge base for fallback
        self.knowledge_base = {
            "nri": {
                "keywords": ["nri", "non resident indian", "non-resident", "foreign", "overseas", "abroad", "nri purchase", "nri buy", "nri property"],
                "answer": """Yes, NRIs (Non-Resident Indians) can purchase property in India, but with certain restrictions:

Allowed:
• Residential properties (apartments, houses, villas)
• Commercial properties (offices, shops)

Not Allowed:
• Agricultural land
• Plantation property
• Farmhouses (in most states)

Key Points:
• NRIs can purchase property without RBI approval
• Property can be purchased in Indian Rupees or foreign currency
• Repatriation of sale proceeds is allowed (up to 2 properties)
• Must comply with FEMA (Foreign Exchange Management Act) regulations
• Property income is taxable in India

Documents Required:
• Valid passport
• PAN card
• Overseas address proof
• NRE/NRO bank account

Note: PIOs (Persons of Indian Origin) and OCIs (Overseas Citizens of India) have similar rights as NRIs."""
            },
            "property_tax": {
                "keywords": ["property tax", "tax", "annual tax", "municipal tax"],
                "answer": """Property tax is an annual tax levied by local municipal authorities on property owners.

Key Points:
• Calculated based on property's annual rental value or capital value
• Varies by city and state
• Must be paid annually
• Non-payment can lead to penalties and legal action

Factors Affecting Property Tax:
• Property location
• Built-up area
• Property age
• Property usage (residential/commercial)

Payment:
• Can be paid online or at municipal offices
• Receipts should be kept as proof
• Some cities offer discounts for early payment"""
            },
            "rera": {
                "keywords": ["rera", "real estate regulation", "builder registration"],
                "answer": """RERA (Real Estate Regulation and Development Act) is a law to protect homebuyers and regulate the real estate sector.

Key Features:
• All builders must register projects with RERA
• Buyers can verify project details online
• Protects against fraud and delays
• Ensures transparency in transactions
• Builders must deposit 70% of funds in escrow account

Benefits for Buyers:
• Standardized carpet area definition
• Mandatory disclosure of project details
• Penalty for delays
• Dispute resolution mechanism

How to Check:
• Visit your state's RERA website
• Search for project registration number
• Verify builder credentials"""
            },
            "sale_deed": {
                "keywords": ["sale deed", "title deed", "ownership document", "property document"],
                "answer": """A Sale Deed is the primary legal document that transfers property ownership from seller to buyer.

Key Points:
• Must be registered with Sub-Registrar office
• Requires stamp duty payment
• Both parties must sign in presence of witnesses
• Becomes legal proof of ownership after registration

Documents Needed:
• Original title documents
• Identity proof of buyer and seller
• PAN cards
• Property tax receipts
• Encumbrance certificate

Important:
• Always verify the seller's ownership before purchase
• Check for any legal disputes or encumbrances
• Consult a lawyer for document verification"""
            },
            "home_loan": {
                "keywords": ["home loan", "mortgage", "loan", "emi", "housing loan"],
                "answer": """Home loans are provided by banks and financial institutions to purchase property.

Eligibility Criteria:
• Minimum age: 21-25 years
• Maximum age: 60-65 years at loan maturity
• Stable income source
• Good credit score (750+)
• EMI should not exceed 40-50% of income

Documents Required:
• Identity proof (Aadhaar, PAN, Passport)
• Address proof
• Income proof (salary slips, ITR)
• Bank statements (6 months)
• Property documents

Loan Amount:
• Usually 75-90% of property value
• Depends on income and credit score

Interest Rates:
• Fixed or floating rates available
• Currently range from 8-10% per annum

Tax Benefits:
• Deduction on principal (Section 80C): Up to ₹1.5 lakh
• Deduction on interest (Section 24): Up to ₹2 lakh"""
            },
            "stamp_duty": {
                "keywords": ["stamp duty", "registration", "registration charges"],
                "answer": """Stamp duty is a tax paid to the state government for registering property documents.

Key Points:
• Mandatory for property registration
• Varies by state (typically 5-7% of property value)
• Must be paid before or during registration
• Can be paid online or at designated banks

Registration Charges:
• Usually 1% of property value
• Separate from stamp duty

Who Pays:
• Typically the buyer
• Can be negotiated between buyer and seller

Exemptions/Concessions:
• Women buyers may get discounts in some states
• First-time buyers may get concessions
• Varies by state government policies"""
            },
            "encumbrance": {
                "keywords": ["encumbrance", "ec", "encumbrance certificate", "clear title"],
                "answer": """An Encumbrance Certificate (EC) shows all transactions related to a property for a specific period.

Purpose:
• Verifies property has no legal dues
• Shows all sales, mortgages, or liens
• Essential for property purchase

What It Shows:
• Previous sales and transfers
• Existing mortgages or loans
• Legal disputes or court cases
• Unpaid dues

How to Obtain:
• Apply at Sub-Registrar office
• Available online in most states
• Requires property details and period

Importance:
• Ensures clear title
• Protects buyer from hidden liabilities
• Required by banks for home loans

Recommendation:
• Get EC for at least 13-30 years
• Verify all transactions are legitimate"""
            },
            "agreement": {
                "keywords": ["agreement to sell", "sale agreement", "mou", "contract"],
                "answer": """An Agreement to Sell is a preliminary contract before the final sale deed.

Key Points:
• Outlines terms and conditions of sale
• Includes property details, price, and payment schedule
• Not the final ownership transfer document
• Must be followed by registered Sale Deed

Contents:
• Property description and address
• Sale price and payment terms
• Possession date
• Penalties for breach
• Rights and obligations of both parties

Legal Status:
• Creates obligation to sell/buy
• Can be enforced in court
• Requires stamp duty (lower than Sale Deed)

Important:
• Should be drafted by a lawyer
• Both parties should understand all terms
• Keep copies for reference"""
            },
            "possession": {
                "keywords": ["possession", "handover", "occupancy certificate"],
                "answer": """Possession is the physical handover of property from seller/builder to buyer.

For Resale Properties:
• Possession given immediately after registration
• Verify all utilities are transferred
• Check for any damages

For New Properties:
• Builder must provide Occupancy Certificate (OC)
• OC confirms building is legally constructed
• Possession should match agreement timeline

Occupancy Certificate:
• Issued by local municipal authority
• Confirms building meets safety standards
• Essential for legal occupation
• Required for utility connections

Delayed Possession:
• Buyer can claim compensation
• RERA provides protection against delays
• Check agreement for penalty clauses

Before Taking Possession:
• Inspect property thoroughly
• Check all fittings and fixtures
• Verify all documents are provided
• Get possession letter from seller/builder"""
            },
            "general": {
                "keywords": ["property", "real estate", "buy", "purchase", "legal"],
                "answer": """I can help you with legal questions about real estate in India.

Common Topics I Can Assist With:
• NRI property purchase rules
• Property documents (Sale Deed, Title Deed, EC)
• RERA regulations
• Home loans and eligibility
• Stamp duty and registration
• Property tax
• Legal checks before buying
• Possession and occupancy certificates

For Specific Questions:
Please ask about a particular topic, and I'll provide detailed legal information.

Important Disclaimer:
The information provided is for general guidance only. Always consult a certified legal expert or property lawyer before making any property transaction."""
            }
        }

    def get_llm(self):
        if self.llm is None:
            try:
                self.llm = ChatGroq(
                    model="llama-3.3-70b-versatile",
                    temperature=0
                )
            except Exception as e:
                print(f"Warning: Could not initialize LLM. {e}")
                self.llm = False
        return self.llm if self.llm is not False else None

    def find_best_match(self, query):
        """Find the best matching answer from knowledge base"""
        query_lower = query.lower()
        
        # Direct keyword matching with scoring
        scores = {}
        for category, data in self.knowledge_base.items():
            score = 0
            for keyword in data["keywords"]:
                if keyword in query_lower:
                    # Give higher score for longer keyword matches
                    score += len(keyword.split()) * 10
            scores[category] = score
        
        # Find category with highest score
        if scores:
            best_match = max(scores, key=scores.get)
            if scores[best_match] > 0:
                return self.knowledge_base[best_match]["answer"]
        
        # Default response if no specific match found
        return self.knowledge_base["general"]["answer"]

    def query(self, query):
        llm_instance = self.get_llm()
        
        # Try AI first if available
        if llm_instance is not None:
            try:
                prompt = f"""
You are a legal property assistant for Indian real estate.

STRICT RULES:
- Give SHORT and PRECISE answers
- ONLY answer what is asked
- Do NOT include:
  - market trends
  - recommendations
  - risks
- Use bullet points if needed
- Stick to legal facts only
- Under NO circumstances should you use Markdown asterisks (**) for bolding.

Context:
{self.knowledge_context}

Question:
{query}

Answer:
"""
                response = llm_instance.invoke(prompt)
                return response.content.strip()
            except Exception as e:
                print(f"AI generation failed: {e}")
                # Fall through to knowledge base
        
        # Use knowledge base fallback
        return self.find_best_match(query)

# Initialize an instance
current_dir = os.path.dirname(__file__)
knowledge_file_path = os.path.join(current_dir, "data", "real_estate_knowledge.txt")
try:
    rag = RAGEngine(knowledge_file_path)
except Exception as e:
    print(f"Warning: Failed to load RAG engine. {e}")
    rag = None
