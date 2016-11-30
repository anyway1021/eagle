/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 * <p>
 * http://www.apache.org/licenses/LICENSE-2.0
 * <p>
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.eagle.app.environment.builder;

import java.util.Map;

/**
 * TODO: Not implemented yet.
 */
public class CEPFunction implements TransformFunction {

    private final CEPDefinition cepDefinition;
    private Collector collector;

    public CEPFunction(CEPDefinition cepDefinition) {
        this.cepDefinition = cepDefinition;
    }

    public CEPFunction(String siddhiQuery, String inputStreamId, String outputStreamId) {
        this.cepDefinition = new CEPDefinition(siddhiQuery,inputStreamId, outputStreamId);
    }

    @Override
    public String getName() {
        return "CEPFunction";
    }

    @Override
    public void open(Collector collector) {
        throw new IllegalStateException("TODO: Not implemented yet");
    }

    @Override
    public void transform(Map event) {
        throw new IllegalStateException("TODO: Not implemented yet");
    }

    @Override
    public void close() {
        throw new IllegalStateException("TODO: Not implemented yet");
    }

    public static class CEPDefinition {
        private String inputStreamId;
        private String outputStreamId;
        private String siddhiQuery;

        public CEPDefinition(String siddhiQuery, String inputStreamId, String outputStreamId) {
            this.siddhiQuery = siddhiQuery;
            this.inputStreamId = inputStreamId;
            this.outputStreamId = outputStreamId;
        }

        public String getSiddhiQuery() {
            return siddhiQuery;
        }

        public void setSiddhiQuery(String siddhiQuery) {
            this.siddhiQuery = siddhiQuery;
        }

        public String getOutputStreamId() {
            return outputStreamId;
        }

        public void setOutputStreamId(String outputStreamId) {
            this.outputStreamId = outputStreamId;
        }

        public String getInputStreamId() {
            return inputStreamId;
        }

        public void setInputStreamId(String inputStreamId) {
            this.inputStreamId = inputStreamId;
        }
    }
}