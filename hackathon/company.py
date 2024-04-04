def get_response(question):
    from libraries import model
    company_info='''Contact Details:

Address: 4th Floor, Block C, Prestige Tech Park, Marathahalli Outer Ring Road, Bangalore - 560037, India
Phone: +91 80 4114 0900
Email: info@aishwi.com
Website: https://www.aishwi.com/
Ashwini Technologies LinkedIn: https://www.linkedin.com/company/aishwi-technologies/?originalSubdomain=in


Projects:

Aishwi Technologies has worked on numerous projects across various industries, including:

Banking and Finance: Digital transformation, mobile banking, core banking solutions
Healthcare: Electronic health records, telemedicine, patient engagement platforms
Retail: E-commerce, omnichannel solutions, loyalty programs
Manufacturing: Industrial IoT, predictive maintenance, supply chain optimization
Government: Smart cities, e-governance, citizen services
Services:

Aishwi Technologies offers a comprehensive range of services, including:

Software Development: Custom software development, mobile app development, web development
Data Analytics: Big data analytics, machine learning, artificial intelligence
Cloud Computing: Cloud migration, cloud infrastructure management, cloud application development
DevOps: Continuous integration and continuous delivery, automated testing, infrastructure automation
Testing: Functional testing, performance testing, security testing
Maintenance and Support: 24/7 support, bug fixes, performance optimization
Consulting: Business process optimization, technology strategy, IT architecture design
Training: Technical training, soft skills training, leadership development
Additional Information:

Aishwi Technologies is a CMMI Level 5 certified company.
The company has over 1,000 employees worldwide.
Aishwi has partnerships with leading technology providers, including Microsoft, Amazon Web Services, and Google Cloud.
The company has been recognized for its excellence in software development and innovation by various industry organizations.

Aishwi Technologies is a leading global provider of software development, data analytics, and cloud computing services. The company was founded in 2003 and is headquartered in Bangalore, India. Aishwi has over 1,000 employees worldwide and serves clients in a variety of industries, including banking and finance, healthcare, retail, manufacturing, and government.

Aishwi's mission is to help clients achieve their business goals through the effective use of technology. The company's team of experienced professionals provides a wide range of services, including:

Software Development: Aishwi offers custom software development services for a variety of platforms, including web, mobile, and cloud. The company's developers have expertise in a wide range of programming languages and technologies.
Data Analytics: Aishwi's data analytics team helps clients extract insights from their data to improve decision-making. The team uses a variety of big data analytics tools and techniques to help clients identify trends, patterns, and anomalies in their data.
Cloud Computing: Aishwi provides cloud computing services to help clients migrate their applications and infrastructure to the cloud. The company's team of cloud experts can help clients with cloud architecture design, implementation, and management.
Aishwi is committed to providing high-quality services to its clients. The company is CMMI Level 5 certified and has a proven track record of success. Aishwi has been recognized for its excellence in software development and innovation by various industry organizations.

Some of Aishwi's key clients include:

Banking and Finance: HDFC Bank, ICICI Bank, Axis Bank
Healthcare: Apollo Hospitals, Fortis Healthcare, Manipal Hospitals
Retail: Reliance Retail, Aditya Birla Retail, Tata Group
Manufacturing: Mahindra & Mahindra, Tata Motors, Ashok Leyland
Government: Government of India, Government of Karnataka, Government of Maharashtra
Aishwi is a trusted partner for businesses of all sizes. The company's commitment to quality and innovation has helped it become one of the leading providers of software development, data analytics, and cloud computing services in the world.
Aishwi Technologies is a CMMI Level 5 certified global provider of software development, data analytics, and cloud computing services. The company was founded in 2003 and is headquartered in Bangalore, India. Aishwi has over 1,000 employees worldwide and serves clients in a variety of industries, including banking and finance, healthcare, retail, manufacturing, and government.
Aishwi's key strengths include:

Deep industry expertise: Aishwi has a deep understanding of the business challenges and technology needs of its clients. The company's team of experienced professionals has worked on numerous projects across a variety of industries, giving Aishwi a unique perspective on how to use technology to solve business problems.
Full-stack capabilities: Aishwi offers a full range of services, from software development and data analytics to cloud computing and infrastructure management. This allows Aishwi to provide clients with a one-stop solution for all of their technology needs.
Commitment to quality: Aishwi is committed to providing high-quality services to its clients. The company's CMMI Level 5 certification is a testament to its commitment to quality and continuous improvement.
Innovation: Aishwi is constantly investing in research and development to stay at the forefront of technology innovation. The company's team of engineers and scientists is working on cutting-edge technologies such as artificial intelligence, machine learning, and blockchain.
Aishwi's clients benefit from the company's deep industry expertise, full-stack capabilities, commitment to quality, and innovation. Aishwi is a trusted partner for businesses of all sizes, helping them to achieve their business goals through the effective use of technology.
Here are some specific examples of how Aishwi has helped its clients:
Banking and Finance: Aishwi helped a leading bank to develop a mobile banking app that has been downloaded over 10 million times. The app allows customers to manage their accounts, make payments, and transfer funds from their mobile devices.
Healthcare: Aishwi helped a hospital to implement a data analytics platform that has improved patient care and reduced costs. The platform allows the hospital to track patient data, identify trends, and predict future health outcomes.
Retail: Aishwi helped a retailer to develop an e-commerce platform that has increased sales by 20%. The platform provides customers with a seamless online shopping experience and allows the retailer to track customer behavior and preferences.
Manufacturing: Aishwi helped a manufacturer to implement a predictive maintenance system that has reduced downtime by 30%. The system uses sensors to monitor equipment and predict when maintenance is needed.
These are just a few examples of how Aishwi is helping its clients to achieve their business goals through the effective use of technology. Aishwi is a trusted partner for businesses of all sizes, providing a wide range of services to help them succeed in the digital age.'''
    instruction='first of all you need to read the given company information here are the company info'+company_info + 'now give me the answer for my query based on given company info here are my query'
    response=model.generate_content(instruction + question)
    return response.text

    