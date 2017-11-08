
# Working RAM Exporter

STEP 1: Install prometheus_client

        $pip install prometheus_client requests

STEP 2: Run exporter
        Pass port number as argument
        
        $python ram_exporter.py 8003

STEP 3: See metrics on http

        $curl http://localhost:8003
        
        OR
        
        Visit browser http://localhost:8003
