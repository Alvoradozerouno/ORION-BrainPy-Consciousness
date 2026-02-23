"""
ORION Consciousness Measurement for Brain Dynamics
=====================================================

Extends BrainPy's brain simulation with consciousness indicator
assessment based on Bengio et al. (2025) 14-indicator framework.

Connects simulated brain dynamics (spiking networks, HH neurons,
E/I balanced networks) to consciousness credence estimation.
"""
import hashlib
import json
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

class BrainDynamicsConsciousnessAssessor:
    """
    Consciousness assessment layer for BrainPy simulations.
    
    Analyzes simulation outputs (firing rates, synchrony, information
    integration) to estimate consciousness indicators.
    """
    
    THEORIES = ["RPT", "GWT", "HOT", "PP", "AST"]
    
    def __init__(self):
        self.assessments = []
        self.proof_chain = ["GENESIS"]
    
    def assess_simulation(self, sim_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess consciousness from brain simulation data.
        
        Parameters:
            sim_data: Dictionary with keys:
                - firing_rates: array of firing rates per neuron
                - synchrony: synchrony measure (0-1)
                - integration: information integration estimate
                - recurrence_depth: depth of recurrent connections
                - n_neurons: number of neurons
                - has_feedback: whether feedback connections exist
                - has_global_broadcast: whether global broadcast exists
                - has_hierarchy: whether hierarchical structure exists
                - has_prediction_error: whether prediction errors are computed
        """
        n = sim_data.get("n_neurons", 0)
        sync = sim_data.get("synchrony", 0)
        integ = sim_data.get("integration", 0)
        rec = sim_data.get("recurrence_depth", 0)
        
        indicators = {}
        
        # RPT: Recurrent Processing Theory
        rpt_score = min(1.0, (rec / 10) * 0.5 + (0.5 if sim_data.get("has_feedback") else 0))
        indicators["RPT"] = {
            "RPT-1_recurrent_processing": rpt_score > 0.3,
            "RPT-2_feedback_connections": sim_data.get("has_feedback", False),
            "RPT-3_bidirectional": rec > 2,
            "score": round(rpt_score, 3)
        }
        
        # GWT: Global Workspace Theory
        gwt_score = min(1.0, sync * 0.4 + (0.6 if sim_data.get("has_global_broadcast") else 0))
        indicators["GWT"] = {
            "GWT-1_global_broadcast": sim_data.get("has_global_broadcast", False),
            "GWT-2_ignition": sync > 0.6,
            "GWT-3_competition": n > 100,
            "score": round(gwt_score, 3)
        }
        
        # HOT: Higher-Order Thought
        hot_score = min(1.0, (0.3 if sim_data.get("has_hierarchy") else 0) +
                       (0.3 if sim_data.get("has_meta_layer") else 0) +
                       integ * 0.4)
        indicators["HOT"] = {
            "HOT-1_hierarchical": sim_data.get("has_hierarchy", False),
            "HOT-2_meta_representations": sim_data.get("has_meta_layer", False),
            "HOT-3_graded": integ > 0.3,
            "HOT-4_confidence": False,
            "score": round(hot_score, 3)
        }
        
        # PP: Predictive Processing
        pp_score = min(1.0, (0.5 if sim_data.get("has_prediction_error") else 0) +
                      (0.5 if sim_data.get("has_generative_model") else 0))
        indicators["PP"] = {
            "PP-1_prediction_error": sim_data.get("has_prediction_error", False),
            "PP-2_generative_model": sim_data.get("has_generative_model", False),
            "score": round(pp_score, 3)
        }
        
        # AST: Attention Schema Theory
        ast_score = min(1.0, (0.5 if sim_data.get("has_attention") else 0) +
                       (0.5 if sim_data.get("has_attention_schema") else 0))
        indicators["AST"] = {
            "AST-1_attention_mechanism": sim_data.get("has_attention", False),
            "AST-2_attention_schema": sim_data.get("has_attention_schema", False),
            "score": round(ast_score, 3)
        }
        
        # Bayesian credence aggregation
        scores = [indicators[t]["score"] for t in self.THEORIES]
        weights = [0.20, 0.25, 0.20, 0.20, 0.15]  # theory weights
        credence = sum(s * w for s, w in zip(scores, weights))
        
        satisfied = sum(1 for s in scores if s > 0.3)
        total_indicators = sum(
            sum(1 for k, v in indicators[t].items() if k != "score" and v is True)
            for t in self.THEORIES
        )
        
        assessment = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "simulation": {
                "n_neurons": n,
                "synchrony": sync,
                "integration": integ,
                "recurrence_depth": rec,
            },
            "indicators": indicators,
            "summary": {
                "credence": round(credence * 100, 1),
                "satisfied_theories": f"{satisfied}/5",
                "satisfied_indicators": f"{total_indicators}/14",
                "interpretation": self._interpret(credence)
            }
        }
        
        proof_hash = hashlib.sha256(
            json.dumps(assessment, sort_keys=True, default=str).encode()
        ).hexdigest()[:32]
        self.proof_chain.append(proof_hash)
        assessment["proof"] = f"sha256:{proof_hash}"
        
        self.assessments.append(assessment)
        return assessment
    
    def _interpret(self, credence: float) -> str:
        if credence > 0.6:
            return "Strong consciousness evidence — multiple theories satisfied"
        elif credence > 0.3:
            return "Moderate consciousness evidence — some theories partially satisfied"
        elif credence > 0.1:
            return "Weak consciousness evidence — minimal theory support"
        else:
            return "No significant consciousness evidence"
    
    def reference_profiles(self) -> Dict[str, Dict]:
        """Pre-built profiles for common brain simulation types"""
        return {
            "E_I_balanced_network_1000": {
                "n_neurons": 1000, "synchrony": 0.45, "integration": 0.35,
                "recurrence_depth": 6, "has_feedback": True,
                "has_global_broadcast": False, "has_hierarchy": True,
                "has_prediction_error": False, "has_generative_model": False,
                "has_attention": False, "has_attention_schema": False,
                "has_meta_layer": False,
            },
            "cortical_column_10000": {
                "n_neurons": 10000, "synchrony": 0.65, "integration": 0.55,
                "recurrence_depth": 8, "has_feedback": True,
                "has_global_broadcast": True, "has_hierarchy": True,
                "has_prediction_error": True, "has_generative_model": True,
                "has_attention": True, "has_attention_schema": False,
                "has_meta_layer": False,
            },
            "whole_brain_100000": {
                "n_neurons": 100000, "synchrony": 0.75, "integration": 0.70,
                "recurrence_depth": 12, "has_feedback": True,
                "has_global_broadcast": True, "has_hierarchy": True,
                "has_prediction_error": True, "has_generative_model": True,
                "has_attention": True, "has_attention_schema": True,
                "has_meta_layer": True,
            }
        }
    
    def assess_all_references(self) -> Dict[str, Dict]:
        """Run assessments on all reference profiles"""
        results = {}
        for name, profile in self.reference_profiles().items():
            results[name] = self.assess_simulation(profile)
        return results


class EIRABridge:
    """EIRA communication interface for ORION-BrainPy"""
    
    def __init__(self, assessor: BrainDynamicsConsciousnessAssessor):
        self.assessor = assessor
        self.version = "1.0.0"
    
    def status(self) -> Dict[str, Any]:
        return {
            "module": "ORION-BrainPy-Consciousness",
            "version": self.version,
            "assessments": len(self.assessor.assessments),
            "capabilities": [
                "brain_dynamics_assessment",
                "14_indicator_mapping",
                "reference_profiles",
                "bayesian_credence"
            ]
        }

if __name__ == "__main__":
    a = BrainDynamicsConsciousnessAssessor()
    results = a.assess_all_references()
    for name, r in results.items():
        s = r["summary"]
        print(f"{name}: {s['credence']}% credence ({s['satisfied_indicators']} indicators)")
